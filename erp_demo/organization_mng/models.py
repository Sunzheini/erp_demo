from django.db import models
from django.utils.text import slugify

from erp_demo.main_app.translator import translate_to_maimunica


class Organization(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
        unique=True,
    )

    eik = models.PositiveIntegerField(
        blank=False, null=False,
    )

    mol = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    address = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    manager_name = models.CharField(
        max_length=99,
        blank=False, null=False,
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
