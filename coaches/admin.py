from django.contrib import admin
from .models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ("name", "display_teams", "specialization")
    list_filter = ("teams",)

    def display_teams(self, obj):
        return ", ".join(team.name for team in obj.teams.all())

    display_teams.short_description = "Teams"