from django.db import models
from teams.models import Team


class Player(models.Model):
    POSITION_CHOICES = [
        ("GK", "Goalkeeper"),
        ("DEF", "Defender"),
        ("MID", "Midfielder"),
        ("FWD", "Forward"),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    profile_photo = models.ImageField(upload_to="players/", blank=True, null=True)
    bio = models.TextField(blank=True)
    joined_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["team", "name"]

    def __str__(self):
        return f"{self.name} ({self.team.name})"
