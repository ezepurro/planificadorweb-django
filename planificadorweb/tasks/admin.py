from django.contrib import admin
from .models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

    # ARREGLO PARA ESTABLECER AL AUTOR COMO EL USUARIO EN USO
    def get_form(self, request, obj=None, **kwargs):
        form = super(TaskAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form

admin.site.register(Task, TaskAdmin)