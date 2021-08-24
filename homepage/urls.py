from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('specialists/', views.CardView.as_view(), name='card_list'),

]
