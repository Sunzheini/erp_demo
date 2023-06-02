from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica


class Risk(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
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

    def __str__(self):
        return f"{self.name}"
