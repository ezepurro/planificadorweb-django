from django.urls import path
from . import views
from .views import Dashboard, TaskDetail

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('add/', views.add_task, name="add_task"),
    path('detail/<int:pk>/', TaskDetail.as_view(), name="task_detail"),

]