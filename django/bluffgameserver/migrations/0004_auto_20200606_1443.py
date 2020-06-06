# Generated by Django 3.0.7 on 2020-06-06 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bluffgameserver', '0003_auto_20200606_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bluffgame',
            name='active_players',
        ),
        migrations.AddField(
            model_name='bluffgame',
            name='players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]