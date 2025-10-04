from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    """
    Represents a media item (movie, book, game, etc.) in the user's tracking system.
    """
    # Status choices
    STATUS_CHOICES = [
        ('', 'Select Status'),
        ('consuming', 'Consuming'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('dropped', 'Dropped'),
        ('planned', 'Planned'),
    ]
    
    # Rating choices (1-10)
    RATING_CHOICES = [
        ('', 'Select Rating'),
        (1, '1 - Terrible'),
        (2, '2 - Very Bad'),
        (3, '3 - Bad'),
        (4, '4 - Poor'),
        (5, '5 - Average'),
        (6, '6 - Fine'),
        (7, '7 - Good'),
        (8, '8 - Very Good'),
        (9, '9 - Great'),
        (10, '10 - Masterpiece'),
    ]

    # Type choices
    TYPE_CHOICES = [
        ('', 'Select Type'),
        ('movie', 'Movie'),
        ('book', 'Book'),
        ('game', 'Game'),
        ('series', 'Series'),
        ('anime', 'Anime'),
        ('manga', 'Manga'),
        ('tv_show', 'TV Show'),
        ('podcast', 'Podcast'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_items', null=True, blank=True)
    title = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title