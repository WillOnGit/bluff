from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import BluffGame
from .forms import NewGameForm

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('lobby'))
    else:
        return HttpResponseRedirect(settings.LOGIN_URL)

def quick_signup(request):
    return HttpResponse("yo")

@login_required
def present_lobby(request):
    games = BluffGame.objects.all()
    return render(request, 'bluffgameserver/lobby.html', {'games': games})

@login_required
def view_game(request, game_id):
    game = get_object_or_404(BluffGame, pk=game_id)
    return render(request, 'bluffgameserver/game_summary.html', {'game': game})

@login_required
def create_game(request):
    if request.method == 'POST':
        # check for bot submissions...
        # ...submitted by person, so process
        if request.POST['mandatory_field']!='':
            return HttpResponseRedirect(reverse('lobby'))
        submission = NewGameForm(request.POST)
        if submission.is_valid():
            print(submission.cleaned_data)
            x = submission.save(commit=False)
            x.creator = request.user
            x.save()
            return HttpResponseRedirect(reverse('game_summary',args=(x.pk,)))
        else:
            return HttpResponse('Your form is invalid, how have you managed that?')
    else:
        form = NewGameForm()

    return render(request, 'bluffgameserver/create_game.html', {'form': form})

@login_required
def join_game(request):
    return HttpResponse("yo")
