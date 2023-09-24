from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import sqlite3
import pandas as pd
import requests
import re
from django.db import connection

from .models import Website


def index(request):
    website_list = Website.objects.order_by("link")
    context = {"website_list": website_list}
    return render(request, "polls/website/index.html", context)

def create(request):
    return render(request, "polls/website/create.html")

def store(request):
    website = Website(name=request.POST["name"], link=request.POST["link"], regex=request.POST["regex"], groups=request.POST["groups"], regex_link=request.POST["regex_link"], groups_link=request.POST["groups_link"], link_comp=request.POST["link_comp"])
    website.save()
    return HttpResponseRedirect(reverse("polls:website-index"))

def show(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    if website.parsed:
        conn = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query(f"SELECT * FROM {website.name}", conn)
        conn.close()
        return render(request, "polls/website/show.html", {"website": website, "df": df})
    else:
        return render(request, "polls/website/show.html", {"website": website})

def edit(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    return render(request, "polls/website/edit.html", {"website": website})

def update(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    website.name=request.POST.get("name", website.name)
    website.link=request.POST.get("link", website.link)
    website.regex=request.POST.get("regex", website.regex)
    website.groups=request.POST.get("groups", website.groups)
    website.regex_link=request.POST.get("regex_link", website.regex_link)
    website.groups_link=request.POST.get("groups_link", website.groups_link)
    website.link_comp=request.POST.get("link_comp", website.link_comp)
    website.save()
    return HttpResponseRedirect(reverse("polls:website-show", kwargs={'website_id':website.id}))

def destroy(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    website.delete()
    return HttpResponseRedirect(reverse("polls:website-index"))

def parse(request, website_id):
    # parse liest die Webseite aus und speichert den Inhalt in der Datenbank als Tabelle website.name
    website = get_object_or_404(Website, pk=website_id)
    groups = website.groups.split(", ")
    response = requests.get(website.link)
    html = response.text
    matches = re.findall(website.regex, html, flags=re.I)
    df = pd.DataFrame(matches)
    i = 0
    for group in groups:
        df = df.rename({i: group}, axis=1)
        i += 1
    conn = sqlite3.connect("db.sqlite3")
    df.to_sql(website.name, conn, if_exists='replace')
    conn.close()

    website.parsed = True
    website.save()
    return HttpResponseRedirect(reverse("polls:website-show", kwargs={'website_id':website.id}))

def parse_link(request, website_id):
    website = get_object_or_404(Website, pk=website_id)
    if website.parsed_link:
        return HttpResponseRedirect(reverse("polls:website-show", kwargs={'website_id':website.id}))
    groups_link = website.groups_link.split(", ")
    conn = sqlite3.connect("db.sqlite3")
    df = pd.read_sql_query(f"SELECT * FROM {website.name}", conn)
    conn.close()
    for group in groups_link:
            df[group] = ""
    for index, row in df.iterrows():
        response = requests.get(website.link_comp + row["Link"])
        html = response.text
        matches = re.findall(website.regex_link, html, flags=re.I)
        df = pd.DataFrame(matches)
        i = 1
        for group in groups_link:
            df.loc[index, group] = df[i][0]
            i += 1
    conn = sqlite3.connect("db.sqlite3")
    df.to_sql(website.name, conn, if_exists='replace')
    conn.close()
    
    website.parsed_link = True
    website.save()
    return HttpResponseRedirect(reverse("polls:website-show", kwargs={'website_id':website.id}))


    