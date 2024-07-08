from django.shortcuts import render
from .models import Task

# Create your views here.

def dashboard(request):
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {'tasks':tasks})


def add_task(request):
    return render(request, "tasks/add_task.html")

def task_detail(request):
    return render(request, "tasks/task_detail.html")

