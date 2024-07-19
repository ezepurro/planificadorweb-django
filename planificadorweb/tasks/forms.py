from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'expiration']        
        widgets = {
            'title': forms.TextInput(attrs={
                'style':'padding: 20px; margin: 20px;',
                'class':'form-control',
                'placeholder':'Tarea a realizar'}
            ),
            'description': forms.Textarea(attrs={
                'style':'padding: 20px; margin: 20px;',
                'class':'form-control',
                'placeholder':'Descripción',
                'id':'exampleFormControlTextarea1',
                'rows':3}
            ),
            'expiration': forms.DateInput(attrs={
                'style':'margin-left: 20px; width: 100%; padding: 20px',
                'class':'form-label',
                'type':'date'}
            ),
        }



