from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('lobby', views.present_lobby, name='lobby'),
        path('game/<int:game_id>/view', views.view_game, name='game_summary'),
        path('game/<int:game_id>/join', views.join_game, name='join_game'),
        path('game/create', views.create_game, name='create_game'),
        ]
