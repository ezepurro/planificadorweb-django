from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from registration.models import Member


class StaffRequiredMixin(object):
    # Sirve para verificar si el usuario es staff
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args,**kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)



class Dashboard(ListView):
    context_object_name = 'members_list'
    model = Member
    template_name = "tasks/task_list.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context.update({
            'tasks_list': Task.objects.order_by('expiration'),            
        })
        return context

    def get_queryset(self):
        return Member.objects.order_by('name')    



class TaskDetail(DetailView):
    model = Task

# Cambiar a TaskCreateView
# @method_decorator(staff_member_required, name='dispatch')
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

    if not request.user.is_staff:
        return redirect('login')

    return render(request, "tasks/add_task.html", {'form': task_form})


@method_decorator(staff_member_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("dashboard")



@method_decorator(staff_member_required, name='dispatch')
class TaskUpdateView(StaffRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("dashboard")


