from django import forms
from .models import Member



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['name', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class':'form-control-file',
                'style':'padding: 20px; margin: 20px;',
            }),
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre',
                'style':'padding: 20px; margin: 20px;',
            }),
        }