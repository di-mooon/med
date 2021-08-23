from django.contrib.auth import authenticate, login
from django.views import View
from django.http import HttpResponseRedirect, Http404
from .forms import ProfilePatientForm, RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ProfilePatient, UserToken
from .service import profile_activate


class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST or None)
        print(request.user)

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
            new_user.residential_address = form.cleaned_data['residential_address']
            new_user.is_active = False
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            profile_activate(new_user.email)

            # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # login(request, user)
            return render(request, 'user/profile_activate.html')
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        user = ProfilePatient.objects.prefetch_related(
            'patient_record__time_patient',
            'patient_record__time_patient__daterecord',
            'patient_record__time_patient__card',
        ).get(username=request.user.username, is_active=True)
        context = {
            'user': user,
        }
        return render(request, 'user/profile.html', context)


class ProfileUpdate(View):
    def get(self, request, *args, **kwargs):
        form = ProfilePatientForm(request.POST or None)
        user = ProfilePatient.objects.get(username=request.user.username, is_active=True)
        form.initial['last_name'] = user.last_name
        form.initial['first_name'] = user.first_name
        form.initial['patronymic'] = user.patronymic
        form.initial['phone'] = user.phone
        form.initial['email'] = user.email
        form.initial['insurance'] = user.insurance
        form.initial['date'] = user.date
        form.initial['residential_address'] = user.residential_address

        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'user/profile_update.html', context)

    def post(self, request, *args, **kwargs):
        form = ProfilePatientForm(request.POST or None, instance=request.user)
        if form.is_valid():
            update_user = form.save(commit=False)
            update_user.last_name = form.cleaned_data['last_name']
            update_user.first_name = form.cleaned_data['first_name']
            update_user.phone = form.cleaned_data['phone']
            update_user.patronymic = form.cleaned_data['patronymic']
            update_user.date = form.cleaned_data['date']
            update_user.insurance = form.cleaned_data['insurance']
            update_user.email = form.cleaned_data['email']
            update_user.residential_address = form.cleaned_data['residential_address']
            update_user.save()
            return HttpResponseRedirect(f"/profile/{request.user.username}/")
        context = {
            'form': form,
        }
        return render(request, 'user/profile_update.html', context)


class ProfileActivate(View):
    def get(self, request, *args, **kwargs):
        try:
            email_token = UserToken.objects.get(token=kwargs.get('token'))
            ProfilePatient.objects.filter(email=email_token.email).update(is_active=True)
            email_token.delete()
        except:
            raise Http404
        return render(request, 'user/profile_confirm.html')
