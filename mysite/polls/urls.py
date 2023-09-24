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
    path("startseite", views.show, name="startseite"),
    path("ueber_uns", views.wir, name="ueber-uns"),
    path("bwki", views.bwki, name="bwki"),
    path("statistiken", views.statistiken, name="statistiken"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("register", views.show_register, name="register"),
    path("register/store", views.store, name="store"),
    path("login", views.show_login, name="login"),
    path("login/action", views.auth, name="auth"),
    path("logout", views.logout_u, name="logout_u"),

    path("websites", website.index, name="website-index"),
    path("websites/create", website.create, name="website-create"),
    path("websites/store", website.store, name="website-store"),
    path("websites/<int:website_id>", website.show, name="website-show"),
    path("websites/<int:website_id>/edit", website.edit, name="website-edit"),
    path("websites/<int:website_id>/update", website.update, name="website-update"),
    path("websites/<int:website_id>/destroy", website.destroy, name="website-destroy"),
    path("websites/<int:website_id>/parse", website.parse, name="website-parse"),
    path("websites/<int:website_id>/parse_link", website.parse_link, name="website-parse_link"),
]
