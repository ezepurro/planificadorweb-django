from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Member
from django import forms
from .forms import ProfileForm

# Create your views here.

class AddMember(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/add_member.html'

    def get_form(self, form_class=None):
        form = super(AddMember, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Usuario',
            'style':'padding: 20px; margin: 20px;',
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Contraseña',
            'style':'padding: 20px; margin: 20px;',
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Repita la contraseña',
            'style':'padding: 20px; margin: 20px;',
        })

        return form
    

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Member.objects.get_or_create(user=self.request.user)
        return profile
    

class MemberDetail(DetailView):
    model = Member
    template_name = 'registration/member_detail.html'