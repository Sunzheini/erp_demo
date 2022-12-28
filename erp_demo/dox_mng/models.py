from django.db import models


class Document(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )
    revision = models.PositiveIntegerField(
        blank=False, null=False,
    )
    owner = models.CharField(
        max_length=30,
        blank=False, null=False,
    )
    attachment = models.FileField(
        blank=False, null=False,
    )
    slug = models.SlugField(
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"
