from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from user.forms import ProfileForm
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def register(request):
    global profile_form
    form=None

    if request.method=='POST':
        form=UserCreationForm(request.POST)

        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request,'пользователь с таким Email зарегистрирован')

        if form.is_valid():
            inc=form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']


            user= authenticate(username=username,password=password, email=email)
            inc.email=email
            inc.save()
            form.save_m2m()
            return redirect("/")
    else:
        form=UserCreationForm()
    context={'form':form


        }
    return render(request,'signup.html',context)

def index(request):
    return render(request,'homepage/index.html')