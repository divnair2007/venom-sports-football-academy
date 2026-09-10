from django.contrib import admin
from .models import TrainingSession

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ("team", "date", "time", "venue", "focus_area")
    list_filter = ("team",)
    date_hierarchy = "date"
