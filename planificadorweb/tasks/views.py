from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
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
    model = Task

    #Si fuera un simple templateview, de esta forma se pasa el diccionario de contexto
    # def get(self, request, *args, **kwargs):
        # tasks = Task.objects.all()
        # return render(request, self.template_name, {'tasks':tasks})


class TaskDetail(DetailView):
    model = Task


def add_task(request):
    task_form = TaskForm()

    if request.method == "POST":
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            current_title = request.POST.get('title', '')
            current_description = request.POST.get('description', '')
            current_expiration = request.POST.get('expiration', '')
            # Cambiar target al usuario correcto
            current_target = request.user
            current_author = request.user
            print("Title:", current_title, "Description:", current_description, "Expiration:", current_expiration, "Target:", current_target, "Author:", current_author)
            new_task = Task(title = current_title, description = current_description, author = current_author, target = current_target, expiration = current_expiration)
            new_task.save()
            return redirect('../dashboard/')

    return render(request, "tasks/add_task.html", {'form': task_form})


