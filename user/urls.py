from django.urls import path
from .views import update_profile, ProfileDetailViews
from . import views
urlpatterns = [
    path('update/', update_profile, name='profile_update'),
    path('<slug:slug>/',views.ProfileDetailViews.as_view(), name='profile'),

    ]