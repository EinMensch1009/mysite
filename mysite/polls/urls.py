from django.urls import path

from . import views, website

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("websites", website.index, name="website_index"),
    path("websites/<int:website_id>/read", website.read, name="website_read"),
    path("startseite", views.show, name="startseite"),
    path("ueber_uns", views.wir, name="ueber-uns"),
    path("bwki", views.bwki, name="bwki"),
    path("statistiken", views.statistiken, name="statistiken"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("register", views.show_register, name="register"),
    path("register/store", views.store, name="store"),
]
