from django.db import models
from teams.models import Team


class Match(models.Model):
    RESULT_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("WIN", "Win"),
        ("LOSS", "Loss"),
        ("DRAW", "Draw"),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches")
    opponent = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=150)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, default="SCHEDULED")
    score_summary = models.CharField(
        max_length=50, blank=True,
        help_text="e.g. 3-1 (filled in once the match is played)",
    )

    class Meta:
        ordering = ["-date", "-time"]

    def __str__(self):
        return f"{self.team.name} vs {self.opponent} on {self.date}"

    @property
    def is_upcoming(self):
        from django.utils import timezone
        return self.date >= timezone.now().date()
