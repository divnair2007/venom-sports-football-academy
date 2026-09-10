from django.views.generic import ListView, DetailView
from .models import Player


class PlayerListView(ListView):
    model = Player
    template_name = "players/player_list.html"
    context_object_name = "players"

    def get_queryset(self):
        qs = super().get_queryset().select_related("team")
        team_id = self.request.GET.get("team")
        if team_id:
            qs = qs.filter(team_id=team_id)
        return qs


class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/player_detail.html"
    context_object_name = "player"
