from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Media(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=30, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True,validators=[MinValueValidator(1), MaxValueValidator(10)])
    genre = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title