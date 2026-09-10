from django.views.generic import TemplateView
from teams.models import Team
from matches.models import Match
from announcements.models import Announcement
from django.utils import timezone


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.now().date()
        ctx["team_count"] = Team.objects.count()
        ctx["next_matches"] = Match.objects.filter(date__gte=today).order_by("date")[:3]
        ctx["latest_announcements"] = Announcement.objects.filter(is_published=True)[:3]
        return ctx


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"
