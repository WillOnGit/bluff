from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('lobby', views.present_lobby, name='lobby'),
        path('game/view/<int:game_id>', views.view_game, name='game_summary'),
        path('game/create', views.create_game, name='create_game'),
        ]
