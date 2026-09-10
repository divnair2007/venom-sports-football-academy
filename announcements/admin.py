from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_by", "published_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "body")
