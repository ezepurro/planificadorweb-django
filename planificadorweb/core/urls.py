from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('task/add/', views.add_task, name="add_task"),
    path('task/detail/', views.task_detail, name="task_detail"),
    path('signin/', views.sign_in, name="sign_in"),
]