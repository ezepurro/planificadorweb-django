from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add/', views.add_task, name="add_task"),
    path('detail/<int:task_id>/', views.task_detail, name="task_detail"),

]