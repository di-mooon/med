from django.forms import ModelForm, Textarea,TextInput,DateInput
from .models import Card_comments,Card


class Card_commentsForm(ModelForm):
    class Meta:
        model=Card_comments
        fields=['comment','data']
        widgets = {

            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите текст"
            }),
            'data': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Введите дату"
            })

        }
