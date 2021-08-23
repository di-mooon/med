from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import RegisterView
from django.contrib import admin

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('<str:pk>/', views.ProfileDetail.as_view(), name='profile'),


]
