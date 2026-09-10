from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "created_at")
    search_fields = ("name", "category")
