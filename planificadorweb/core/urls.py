from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('/member/add', views.add_member, name="add_member"),
    path('/task/add', views.add_task, name="add_task"),
    path('/member/detail', views.member_detail, name="member_detail"),
    path('/task/detail', views.task_detail, name="task_detail"),
    path('/signin', views.sign_in, name="sign_in"),
]