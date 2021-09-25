from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=20, null=False, primary_key=True)
