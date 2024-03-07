from django.shortcuts import render
# Create your views here.



def home(request):
    return render(request, "core/home.html")

def add_task(request):
    return render(request, "core/add_task.html")

def task_detail(request):
    return render(request, "core/task_detail.html")

def sign_in(request):
    return render(request, "core/sign_in.html")