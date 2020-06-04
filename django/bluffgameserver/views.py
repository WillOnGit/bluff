from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This will eventually be a quick signup page, simply asking for a name before redirecting to /lobby. Do that manually for now!")

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
