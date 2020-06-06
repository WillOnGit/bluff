from django.contrib.auth.models import User
from django.db import models

class BluffGame(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    #opponent = models.ForeignKey(
    #    User, related_name='opponent', null=True, blank=True)
    max_players = models.IntegerField(default=4)
    active_players = models.IntegerField(default=0)

    date_started = models.DateTimeField(null=True, blank=True)
    has_started = models.BooleanField(default=False)
    # initially just support for one round per player
    current_round = models.IntegerField(default=0)
    current_turn = models.ForeignKey(User, related_name='current_turn', on_delete=models.PROTECT, null=True, blank=True)

    has_completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(User, related_name='winner', null=True, blank=True, on_delete=models.PROTECT)

    # methods
    def __str__(self):
        return self.name

    def start_game(self):
        # set started date + has started, prevent players from joining, start round 1
        pass

    def new_round(self):
        # while game not over, increment round counter and implement round
        pass

    def complete_game(self):
        # declare winner, set has completed and date complete
        pass
