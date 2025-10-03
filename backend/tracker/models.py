from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    """
    Represents a media item (movie, book, game, etc.) in the user's tracking system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_items', null=True, blank=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=30, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title