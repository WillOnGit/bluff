from django.contrib import admin
from .models import BluffGame

class BluffAdmin(admin.ModelAdmin):
    pass
admin.site.register(BluffGame,BluffAdmin)
