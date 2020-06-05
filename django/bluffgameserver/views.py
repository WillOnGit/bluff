from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('lobby'))
    else:
        return HttpResponseRedirect(settings.LOGIN_URL)

def quick_signup(request):
    return HttpResponse("yo")

def present_lobby(request):
    return render(request, 'bluffgameserver/lobby.html')

def create_game(request):
    return HttpResponse("yo")

def join_game(request):
    return HttpResponse("yo")

def view_game(request):
    return HttpResponse("yo")
