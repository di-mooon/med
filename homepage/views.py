from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Card
from .servise import create_cards_list


class CardViews(View):
    def get(self, request, **kwargs):
        cards = Card.objects.all().prefetch_related('card_time')
        cards_list = create_cards_list(cards)
        context = {
            'cards': cards_list,
        }
        return render(request, 'homepage/card_list.html', context)


