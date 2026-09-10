from django.views.generic import ListView
from .models import TrainingSession


class TrainingListView(ListView):
    model = TrainingSession
    template_name = "training/training_list.html"
    context_object_name = "sessions"
