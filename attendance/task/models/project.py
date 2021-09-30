from django.db import models

from .tag import Tag


class Project(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField()

    def __str__(self):
        return self.name


class Project2(models.Model):
    name = models.CharField(max_length=20)
    tags = models.ManyToManyField(to=Tag)
    note = models.TextField()

    def __str__(self):
        return self.name
