from django.utils import timezone
from django.views.generic import ListView
from .models import Match


class MatchListView(ListView):
    """Shows upcoming matches and past results, per FR-07."""
    model = Match
    template_name = "matches/match_list.html"
    context_object_name = "matches"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["upcoming"] = Match.objects.filter(
            result="SCHEDULED"
        ).select_related("team")

        ctx["past"] = Match.objects.exclude(
            result="SCHEDULED"
        ).select_related("team")

        return ctx