from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput, EmailInput


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username','first_name','last_name', 'email', 'password1', 'password2']
