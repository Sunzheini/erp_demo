import datetime

from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica


class MeasuringEquipment(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    inventory_number = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    characteristics = models.TextField(
        blank=True, null=True,
    )

    installation_date = models.DateField(
        blank=True, null=True,
    )

    calibration_interval_in_days = models.IntegerField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def distance_to_calibration_deadline(self):
        if self.installation_date is None or self.calibration_interval_in_days is None:
            return None
        timedelta = (self.installation_date + datetime.timedelta(
            days=self.calibration_interval_in_days)) - datetime.date.today()
        return timedelta.days

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
