from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica


class Kpi(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    target = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    actual_01_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_02_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_03_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_04_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_05_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_06_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_07_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_08_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_09_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_10_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_11_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    actual_12_23 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
