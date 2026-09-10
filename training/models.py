from django.db import models
from teams.models import Team


class TrainingSession(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="training_sessions")
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=150)
    focus_area = models.CharField(
        max_length=100, blank=True,
        help_text="e.g. Fitness, Tactics, Set Pieces",
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["date", "time"]
        verbose_name = "Training Session"

    def __str__(self):
        return f"{self.team.name} training on {self.date}"
