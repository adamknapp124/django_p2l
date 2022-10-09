from django.contrib import admin

from .models import Game, GameScore

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['game_name', 'high_score', 'last_played']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('game_name', 'high_score', 'last_played')

        return()