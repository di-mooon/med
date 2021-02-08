from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Card, Card_comments
from .forms import Card_commentsForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class CardViews(View):

    def get(self,request):
        card=Card.objects.all()
        return render(request, 'homepage/index.html', {'card':card})

def appointment(request):
    return render(request,'appointment/appointment.html')

class Card_commentsDetailViews(View):

    def get(self, request, pk):
        card_comments=Card.objects.get(id=pk)
        return render(request, 'comments/comments.html', {'card_comments': card_comments})

def create_comments(request,pk):
    error = ''
    if request.method == 'POST':
        form = Card_commentsForm(request.POST)

        if form.is_valid():
            form=form.save(commit=False)
            form.card_id=pk
            form.user = request.user
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена неверно'

    form = Card_commentsForm()
    context = {'form': form,
               'error': error
               }
    return render(request, 'comments/creat_comments.html', context)

