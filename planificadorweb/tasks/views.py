# from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from registration.models import Member
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



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



@method_decorator(staff_member_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("dashboard")
    form_class = TaskForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.target= User.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(TaskCreateView, self).form_valid(form)

"""
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] =  User.objects.all()
        context['user'] = get_object_or_404(User, pk=self.kwargs['pk'])
        print(context['user'])
        return context
"""  


@method_decorator(staff_member_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("dashboard")



@method_decorator(staff_member_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("dashboard")


