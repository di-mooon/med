from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register
from django.contrib import admin
urlpatterns = [
    path('signup/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='login'),name='login')


    ]