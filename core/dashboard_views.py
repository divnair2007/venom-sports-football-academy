"""
Custom secure admin dashboard (distinct from /admin, Django's built-in
admin). Implements FR-01 (login), FR-02 (restricted access), FR-15
(logout) and the two-panel layout described in the System Design doc
section 1.3 (fixed sidebar + content panel).

This gives you a branded dashboard to layer on top of the quick-win
Django admin from build step 4 -- add ModelForm-based add/edit/delete
views per module here (or in each app's own views.py) following the
same pattern as PlayerListView etc.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from teams.models import Team
from players.models import Player
from coaches.models import Coach
from matches.models import Match
from training.models import TrainingSession
from announcements.models import Announcement


def admin_login(request):
    if request.user.is_authenticated:
        return redirect("admin_dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")
        messages.error(request, "Invalid credentials or insufficient permissions.")

    return render(request, "admin_panel/login.html")


@login_required(login_url="admin_login")
def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


@login_required(login_url="admin_login")
def admin_dashboard(request):
    """Landing page of the admin dashboard: quick counts per module,
    matching the sidebar modules in the System Design doc (Players,
    Coaches, Teams, Matches, Training, Announcements)."""
    context = {
        "team_count": Team.objects.count(),
        "player_count": Player.objects.count(),
        "coach_count": Coach.objects.count(),
        "match_count": Match.objects.count(),
        "training_count": TrainingSession.objects.count(),
        "announcement_count": Announcement.objects.count(),
    }
    return render(request, "admin_panel/dashboard.html", context)
