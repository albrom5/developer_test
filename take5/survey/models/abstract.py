from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('criada em', auto_now_add=True)
    edited_at = models.DateTimeField('alterada em', auto_now=True)

    class Meta:
        abstract = True
