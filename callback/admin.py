from django.contrib import admin

from callback.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'players')
    search_fields = ('name', 'email')



admin.site.register(Player, PlayerAdmin)

