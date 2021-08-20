from django.urls import path

from . import views

urlpatterns = [
    path('create-record/<int:pk>/<int:p>/<int:k>/', views.RecordTimeView.as_view(), name='record-create'),
]
