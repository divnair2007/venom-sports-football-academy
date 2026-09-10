from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "team", "position", "age")
    list_filter = ("team", "position")
    search_fields = ("name",)
