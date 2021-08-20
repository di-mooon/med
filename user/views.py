from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages


def update_profile(request):
    if request.method == 'POST':

        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Вы успешно отредактировали свой профиль')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:

        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/profile_update.html', {

        'profile_form': profile_form
    })
