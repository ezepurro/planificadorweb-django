from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='members', null=True, blank=True)