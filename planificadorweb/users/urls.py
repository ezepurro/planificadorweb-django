from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.member_detail, name="member_detail"),
]