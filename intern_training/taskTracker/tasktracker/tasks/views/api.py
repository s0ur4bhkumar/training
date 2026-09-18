from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.parsers import JSONParser

from ..models import Task
from ..serializers import TaskSerializer, UserSerializer


@csrf_exempt
def TaskListApiView(request):
    """
    list all tasks and create
    """
    authentication_classes = {SessionAuthentication}
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    if request.method == "GET":
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def taskDetailApiView(request, pk):
    """
    test for update and delete
    """
    authentication_classes = {SessionAuthentication}
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
    ]
    try:
        task = Task.objects.get(pk=pk)
    except task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return JsonResponse(data=serializer.data, safe=False)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        task.delete()
        return HttpResponse(status=204)


def userList(request):
    Authentication_classes = {SessionAuthentication}
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
