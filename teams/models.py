from django.db import models


class Team(models.Model):
    """A team / age category (e.g. U-14 Boys, Senior Men). Every Player,
    Coach, Match and Training record references a Team by foreign key
    rather than repeating team details, per the 3NF normalization note
    in the System Design doc (section 3.4)."""

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=50,
        help_text="e.g. U-12, U-16, Senior Men, Senior Women",
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"
