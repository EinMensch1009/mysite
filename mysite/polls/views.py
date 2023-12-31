from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .models import Question, Choice

def store(request):
    user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
    user.last_name = request.POST["last_name"]
    user.first_name = request.POST["first_name"]
    user.save()
    login(request, user)
    return HttpResponseRedirect(reverse("polls:startseite"))

def auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("polls:startseite"))
    else:
        return render(request, "polls/login.html", {"error": "Passwort oder Nutzername falsch oder noch nicht registriert! Überprüf das mal!"})
        
def show(request):
    return render(request, "polls/startseite.html")

def logout_u(request):
    logout(request)
    return HttpResponseRedirect(reverse("polls:startseite"))

def show_register(request):
    return render(request, "polls/register.html")

def wir(request):
    return render(request, "polls/ueber_uns.html")

def show_login(request):
    return render(request, "polls/login.html")

def bwki(request):
    return render(request, "polls/bwki.html")

def tutorial(request):
    return render(request, "polls/tutorial.html")

def statistiken(request):
    return render(request, "polls/statistiken.html")

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


