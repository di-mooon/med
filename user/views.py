from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.views.generic.base import View
from django.views.generic import DetailView


class ProfileDetailViews(DetailView):
        model = Profile
        context_object_name = 'profile'
        template_name = 'user/profile.html'

        #def get_queryset(self):
            #return Profile.objects.get(user__username=self.kwargs.get("slug"))



def update_profile(request):
    if request.method == 'POST':

        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if  profile_form.is_valid():

            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:

        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/profile_update.html', {

        'profile_form': profile_form
    })