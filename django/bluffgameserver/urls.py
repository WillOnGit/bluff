from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('lobby', views.present_lobby, name='lobby'),
        ]
