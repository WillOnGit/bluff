from django.forms import ModelForm
from .models import BluffGame

class NewGameForm(ModelForm):
    class Meta:
        model = BluffGame
        fields = ['name','max_players']
