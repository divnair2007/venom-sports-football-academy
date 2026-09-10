"""
Root URL configuration.
Public routes live under each app's own urls.py (included with no prefix,
per the flat public site map in the System Design doc). Django's built-in
admin stays at /admin for the "quick backend win" (see build guide step 4);
the custom admin dashboard lives at /dashboard/.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public site
    path("", include("core.urls")),
    path("teams/", include("teams.urls")),
    path("players/", include("players.urls")),
    path("coaches/", include("coaches.urls")),
    path("matches/", include("matches.urls")),
    path("training/", include("training.urls")),
    path("announcements/", include("announcements.urls")),

    # Custom secure admin dashboard (FR-01 to FR-15)
    path("dashboard/", include("core.dashboard_urls")),
]
