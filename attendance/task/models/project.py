from django.db import models

from .tag import Tag



class Project(models.Model):
    name = models.CharField(max_length=20)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField()

    def __str__(self):
        return self.name
