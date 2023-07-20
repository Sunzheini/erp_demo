from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica


class StatModel1(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50

    class Meta:
        ordering = ['id']

    # unique subsequent number (1, 2, 3, ...)
    name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
    )

    operator = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    grinding = models.PositiveIntegerField(
        blank=False, null=False,
    )

    welding = models.PositiveIntegerField(
        blank=False, null=False,
    )

    blasting = models.PositiveIntegerField(
        blank=False, null=False,
    )

    painting = models.PositiveIntegerField(
        blank=False, null=False,
    )

    assembly = models.PositiveIntegerField(
        blank=False, null=False,
    )

    total_pieces = models.PositiveIntegerField(
        blank=False, null=False,
    )

    slug = models.SlugField(
            blank=True, null=True,
            editable=False,
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            name_to_str = str(self.name)
            self.slug = slugify(f"{translate_to_maimunica(name_to_str[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
