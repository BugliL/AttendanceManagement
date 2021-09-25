from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)

