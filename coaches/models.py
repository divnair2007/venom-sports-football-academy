from django.db import models
from teams.models import Team


class Coach(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(
        max_length=100,
        help_text="e.g. Goalkeeping, Fitness, Youth Development",
    )
    experience_years = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="coaches/", blank=True, null=True)
    bio = models.TextField(blank=True)

    teams = models.ManyToManyField(
        Team,
        blank=True,
        related_name="coaches",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name