from django.db import models
from django.utils import timezone

from .tag import Tag


class Event(models.Model):
    date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField()
