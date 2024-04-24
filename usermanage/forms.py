from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class signIn_form(AuthenticationForm):
      class Meta:
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }


class signUp_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'required'}),
        }