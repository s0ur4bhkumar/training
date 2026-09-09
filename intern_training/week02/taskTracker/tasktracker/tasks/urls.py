from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.details, name="details"),
    path("about/", views.about, name="about"),
]
