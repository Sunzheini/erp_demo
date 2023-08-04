import datetime

from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica


class Machine(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
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

    maintenance_interval_in_days = models.IntegerField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def distance_to_maintenance_deadline(self):
        if self.installation_date is None or self.maintenance_interval_in_days is None:
            return None
        timedelta = (self.installation_date + datetime.timedelta(
            days=self.maintenance_interval_in_days)) - datetime.date.today()
        return timedelta.days

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")

        try:
            return super().save(*args, **kwargs)
        except ValidationError as v_error:
            print(f"ValidationError: {v_error}")
            raise
        except IntegrityError as i_error:
            print(f"IntegrityError: {i_error}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def __str__(self):
        return f"{self.name}"
