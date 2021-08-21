from django.contrib.auth import authenticate, login
from django.views import View

from .forms import ProfilePatientForm, RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ProfilePatient


class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('card_list')
        context = {
            'form': form,
        }
        return render(request, 'user/login.html', context)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.last_name = form.cleaned_data['last_name']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.phone = form.cleaned_data['phone']
            new_user.patronymic = form.cleaned_data['patronymic']
            new_user.date = form.cleaned_data['date']
            new_user.insurance = form.cleaned_data['insurance']
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('card_list')
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        user = ProfilePatient.objects.get(username=request.user.username)
        context = {
            'user': user,
        }
        return render(request, 'user/profile.html', context)

class ProfileUpdate(View):
    def get(self, request, *args, **kwargs):
        user = ProfilePatient.objects.get(username=request.user.username)
        context = {
            'user': user,
        }
        return render(request, 'user/profile-update.html', context)