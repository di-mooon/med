from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Card_commentsDetailViews.as_view(), name='comments'),
    path('specialists/', views.CardViews.as_view(), name='card_list'),

]
