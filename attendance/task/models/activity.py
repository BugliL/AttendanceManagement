from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .project import Project
from .event import Event
from .tag import Tag


class Activity(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, related_name='activities', on_delete=models.PROTECT, null=False, blank=False)
    event = models.ForeignKey(Event, related_name='activities', on_delete=models.PROTECT, null=True, blank=True)
    project = models.ForeignKey(Project, related_name='activities', on_delete=models.PROTECT, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='activities')
    hours = models.DecimalField(max_digits=4, decimal_places=1)
    note = models.TextField(blank=True)

    def tags_str(self):
        return Tag.to_string(self)

    def format_day(self):
        return "{}{}".format(self.tags_str(), self.hours)

    def __str__(self):
        tags = Tag.to_string(self)
        return "{} {} {:-5} {}, {}".format(self.date, self.user, self.hours, tags, self.project)

    class Meta:
        verbose_name_plural = "activities"
