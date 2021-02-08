from django.urls import path
from . import views

urlpatterns = [
    path('', views.CardViews.as_view(), name='home'),
    path('<int:pk>/', views.Card_commentsDetailViews.as_view(), name='comments'),
    path('creat_comments/<int:pk>/', views.create_comments, name='creat_comments'),
    path('appointment/', views.appointment, name='appointment')

]
