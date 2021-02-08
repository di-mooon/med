from django.forms import ModelForm,TextInput, EmailInput, DateInput,ImageField
from .models import Profile, User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','patronymic','phone','insurance','email_two','avatar','data']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Иван"
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Иванов"
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Иванович"
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "+7(___)-___-__-__"
            }),
            'insurance': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "СНИЛС"
            }),
            'email_two': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "example@gmail.com"
            }),
            'data': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Введите дату рождения"
            })



        }