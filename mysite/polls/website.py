from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Website


def index(request):
    websites = Website.objects.all()
    context = {"websites": websites}
    return render(request, "polls/website_index.html", context)
