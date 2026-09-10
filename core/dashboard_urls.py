from django.urls import path
from . import dashboard_views

urlpatterns = [
    path("login/", dashboard_views.admin_login, name="admin_login"),
    path("logout/", dashboard_views.admin_logout, name="admin_logout"),
    path("", dashboard_views.admin_dashboard, name="admin_dashboard"),
    # Add per-module manage/add/edit/delete routes here as you build them, e.g.:
    # path("players/", include("players.dashboard_urls")),
]
