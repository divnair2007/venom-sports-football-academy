from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("team", "opponent", "date", "time", "venue", "result")
    list_filter = ("team", "result")
    date_hierarchy = "date"
