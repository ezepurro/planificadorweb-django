from django.urls import path
from . import views
from .views import Dashboard, TaskDetail, add_task

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', add_task, name="add_task"),
    path('detail/<int:pk>/', TaskDetail.as_view(), name="task_detail"),

]