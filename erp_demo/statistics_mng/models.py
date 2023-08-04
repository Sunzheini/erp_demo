from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica


class StatModel1(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    # unique subsequent number (1, 2, 3, ...)
    name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    operator = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
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

    def clean(self):
        if len(self.name) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Name must be longer than 1 character!')

        if len(self.operator) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Operator must be longer than 1 character!')

    def save(self, *args, **kwargs):
        if not self.slug:
            name_to_str = str(self.name)
            self.slug = slugify(f"{translate_to_maimunica(name_to_str[0:30])}")

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
