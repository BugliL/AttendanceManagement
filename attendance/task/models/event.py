from django.db import models
from django.utils import timezone

from .tag import Tag


class Event(models.Model):
    date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        tags = ", ".join([t.text for t in self.tags.all().order_by('text')])
        return "{} - {}: {}".format(self.date.isoformat(), self.note, tags)
