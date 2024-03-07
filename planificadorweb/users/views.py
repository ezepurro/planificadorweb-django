from django.shortcuts import render

# Create your views here.

def member_detail(request):
    return render(request, "users/member_detail.html")

def add_member(request):
    return render(request, "users/add_member.html")

