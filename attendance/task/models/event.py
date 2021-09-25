import textwrap

from django.db import models
from django.utils import timezone

from .tag import Tag


class Event(models.Model):
    date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        tags = Tag.to_string(self)
        # note = textwrap.shorten(self.note, width=20)
        return "{} - {}".format(self.date.isoformat(), tags)
