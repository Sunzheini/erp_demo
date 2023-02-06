from django.db import models


class CaptainsLog(models.Model):
    class Meta:
        ordering = ['id']

    operation = models.CharField(
        max_length=90,
        blank=False, null=False,
    )

    # ToDo: fix format
    performed_at_time = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    execution_time = models.CharField(
        max_length=30,
        blank=False, null=False,
    )
