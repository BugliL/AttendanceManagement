from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .tag import Tag


class Activity(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, related_name='following', on_delete=models.PROTECT)
    tags = models.ManyToManyField(to=Tag)
    hours = models.DecimalField(max_digits=4, decimal_places=1)
    note = models.TextField()
