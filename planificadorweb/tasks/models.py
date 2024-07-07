from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    expiration = models.DateField(verbose_name="Fecha de expiración")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        ordering = ['-created']

    def __str__(self):
        return self.title