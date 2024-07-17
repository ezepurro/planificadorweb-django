from django.shortcuts import render

# Create your views here.

def member_detail(request):
    return render(request, "users/member_detail.html")


