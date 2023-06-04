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

    description = models.TextField(
        blank=True, null=True,
    )

    probability = models.IntegerField(
        blank=False, null=False,
    )

    impact = models.IntegerField(
        blank=False, null=False,
    )

    immediate_action = models.TextField(
        blank=True, null=True,
    )

    ia_test_period = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    long_term_action = models.TextField(
        blank=True, null=True,
    )

    new_probability = models.IntegerField(
        blank=True, null=True,
    )

    new_impact = models.IntegerField(
        blank=True, null=True,
    )

    @property
    def value(self):
        return self.probability * self.impact

    @property
    def new_value(self):
        if self.new_probability is None or self.new_impact is None:
            return None
        return self.new_probability * self.new_impact

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
