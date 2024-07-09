from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(label="Titulo", required=True, widget=forms.TextInput(
        attrs={'style':'padding: 20px; margin: 20px;',
               'class':'form-control',
               'placeholder':'Tarea a realizar'}
    ))
    description = forms.CharField(label="Descripción", widget=forms.Textarea(
        attrs={'style':'padding: 20px; margin: 20px;',
               'class':'form-control',
               'placeholder':'Descripción',
               'id':'exampleFormControlTextarea1',
               'rows':3}
    ))
    expiration = forms.DateField(label="Fecha de expiración", required=True, widget=forms.DateInput(
        attrs={'style':'margin-left: 20px; color: white; width: 100%; padding: 20px',
               'class':'form-label',
               'type':'date'}
    ))