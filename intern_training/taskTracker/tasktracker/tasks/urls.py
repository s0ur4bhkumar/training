from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.Home, name="Home"),
    path("tasks_lists/", views.tasks_list, name="tasks_list"),
    path("about/", views.about, name="about"),
    path("create/", views.task_create, name="create_task"),
    path("update/<int:pk>", views.task_update, name="update_task"),
    path("delete/<int:pk>/", views.task_delete, name="delete_task"),
    path("task_details/<int:pk>", views.task_detail, name="task_details"),
]
