from django.core import paginator
from django.core.paginator import PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView

from .forms import TaskForm
from .models import Task


def Home(request):
    return render(request, "tasks/Home.html")


def tasks_list(request):
    task_list = Task.objects.all()
    paginator = Paginator(task_list, 5)

    try:
        page_num = request.GET.get("page")
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    else:
        page_obj = paginator.get_page(page_num)

    return render(request, "tasks/tasks.html", context={"pages": page_obj})


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)

    return render(request, "tasks/task_details.html", context={"task": task})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/tasks_lists")
    else:
        form = TaskForm
    return render(request, "tasks/form.html", context={"form": form})


def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/tasks_lists")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/form.html", context={"form": form})


def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("/tasks_lists")

    return render(request, "tasks/confirmation.html", {"task": task})


def about(request):
    return render(request, "tasks/about.html")
