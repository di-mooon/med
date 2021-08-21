from django.forms import ModelForm, TextInput, EmailInput, DateInput, ImageField
from .models import ProfilePatient, ProfileDoctor, User

from django.db.models import Q
from django import forms
from django.forms import TextInput, EmailInput


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['confirm_password'].label = 'Подтверждение пароля'
        self.fields['password'].label = 'Пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['patronymic'].label = 'Отчество'
        self.fields['date'].label = 'Дата рождения'
        self.fields['phone'].label = 'Моб.телефон'
        # self.fields['residential_address'].label = 'Адрес проживания'
        self.fields['email'].label = 'Email'
        self.fields['insurance'].label = 'СНИЛС'

    def clean_email(self):
        email = self.cleaned_data['email']
        if ProfilePatient.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый ящик уже зарегистрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if ProfilePatient.objects.filter(username=username).exists():
            raise forms.ValidationError('Данный логин уже зарегистрирован')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = ProfilePatient
        fields = ['username', 'password',
                  'confirm_password', 'first_name',
                  'last_name', 'patronymic', 'date',
                  'phone', 'email', 'insurance', ]
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
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "example@gmail.com"
            }),
            'date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Введите дату рождения"
            })

        }


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин или Email'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not ProfilePatient.objects.filter(Q(username=username) | Q(email=username)):
            raise forms.ValidationError('Пользователь не найден')

        user = ProfilePatient.objects.filter(Q(username=username) | Q(email=username)).first()

        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')

        return self.cleaned_data

    class Meta:
        model = ProfilePatient
        fields = ['username', 'password']


class ProfilePatientForm(forms.ModelForm):
    class Meta:
        model = ProfilePatient
        fields = ['first_name', 'last_name', 'patronymic', 'phone', 'insurance', 'email', 'avatar', 'date']
