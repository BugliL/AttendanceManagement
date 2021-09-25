from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.text

    @classmethod
    def to_string(cls, entity):
        return ", ".join([t.text for t in entity.tags.all().order_by('text')])

    class Meta:
        ordering = ('text',)
