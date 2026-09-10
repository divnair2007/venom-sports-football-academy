from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="announcements")
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
