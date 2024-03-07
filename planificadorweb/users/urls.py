from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.member_detail, name="member_detail"),
    path('add/', views.add_member, name="add_member"),

]