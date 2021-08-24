import asyncio

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView, PasswordChangeView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.views.generic import UpdateView, CreateView

from .forms import ProfilePatientForm, RegistrationForm, LoginForm, PasswordResetUserForm, SetPasswordUserForm, \
    PasswordChangeUserForm
from .models import ProfilePatient
from .service import profile_activate


class LoginUserView(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        return f"/accounts/{self.request.POST.get('username', '')}"


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'
    success_url = 'activate'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()
        profile_activate(self.request, new_user)
        return render(self.request, 'registration/activate_account.html')


class PasswordChangeUserView(PasswordChangeView):
    form_class = PasswordChangeUserForm


class PasswordResetUserView(PasswordResetView):
    form_class = PasswordResetUserForm
    email_template_name = 'send_mail/password_reset_email.html'


class PasswordResetConfirmUserView(PasswordResetConfirmView):
    form_class = SetPasswordUserForm


class ProfileActivate(View):
    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs.get('uidb64')))
            user = ProfilePatient.objects.get(pk=uid)
            print(uid)
            if user is not None and default_token_generator.check_token(user, kwargs.get('token')):
                user.is_active = True
                user.save()
        except:
            raise Http404
        return render(request, 'registration/confirm_account.html')


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        try:
            user = ProfilePatient.objects.prefetch_related(
                'patient_record__time_patient',
                'patient_record__time_patient__daterecord',
                'patient_record__time_patient__card',
            ).get(username=request.user.username, is_active=True)
        except:
            raise Http404
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
            return HttpResponseRedirect(f"/accounts/{self.request.user.username}/")
        context = {
            'form': form,
        }
        return render(request, 'user/profile_update.html', context)

# class ProfileUpdateView(UpdateView):
#     template_name = 'user/profile_update.html'
#     fields = ['last_name', 'first_name']
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'
#
#     def get_success_url(self):
#         return f"/profile/{self.request.user.username}/"
#
#     def get_queryset(self):
#         return ProfilePatient.objects.filter(username=self.request.user.username, is_active=True)
