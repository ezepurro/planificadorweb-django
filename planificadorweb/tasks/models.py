from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    isDone = models.BooleanField(default=False, verbose_name="Tarea realizada")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, default="", related_name='%(class)s_author')
    target = models.ForeignKey(User, verbose_name="Destinatario", on_delete=models.CASCADE, related_name='%(class)s_target', default="")
    expiration = models.DateField(verbose_name="Fecha de expiración")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-created']

    def __str__(self):
        return self.title
    