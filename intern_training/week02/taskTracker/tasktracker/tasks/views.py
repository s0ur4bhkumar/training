from django.http import HttpResponse
from django.shortcuts import render


def tasks(request):
    context = {"tasks": ["task1", "task2", "task3", "task4"]}
    return render(request, "tasks/index.html", context)
