from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def dashboard(request):
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {'tasks':tasks})



def add_task(request):
    task_form = TaskForm()

    if request.method == "POST":
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            expiration = request.POST.get('expiration', '')
            print(expiration)
            return redirect('../dashboard/')

    return render(request, "tasks/add_task.html", {'form': task_form})



def task_detail(request, task_id): 
    task = get_object_or_404(Task, id=task_id)
    return render(request, "tasks/task_detail.html", {'task':task})

