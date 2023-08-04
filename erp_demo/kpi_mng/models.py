from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica


class Kpi(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    description = models.TextField(
        blank=True, null=True,
    )

    target = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    actual_01_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_02_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_03_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_04_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_05_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_06_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_07_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_08_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_09_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_10_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_11_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    actual_12_23 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.target) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Target must be longer than 1 character!')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")

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
