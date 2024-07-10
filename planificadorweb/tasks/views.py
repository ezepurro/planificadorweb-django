from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from .forms import TaskForm

# FUNCTION-BASED VIEW
"""
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {'tasks':tasks})
"""

# CLASS-BASED VIEW
class Dashboard(ListView):
    # template_name = "tasks/dashboard.html"
    model = Task

    # def get(self, request, *args, **kwargs):
        # tasks = Task.objects.all()
        # return render(request, self.template_name, {'tasks':tasks})

# ---


class TaskDetail(DetailView):
    model = Task


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

