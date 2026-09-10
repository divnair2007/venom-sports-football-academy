from django.views.generic import ListView, DetailView
from .models import Coach


class CoachListView(ListView):
    model = Coach
    template_name = "coaches/coach_list.html"
    context_object_name = "coaches"


class CoachDetailView(DetailView):
    model = Coach
    template_name = "coaches/coach_detail.html"
    context_object_name = "coach"
