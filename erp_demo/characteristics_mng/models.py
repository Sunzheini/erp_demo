from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


characteristic_type_choices = [
    ('Product', 'Product'),
    ('Process', 'Process'),
]


class Characteristic(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MAX_LENGTH_LONG = 199
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    code = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False,
        null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        choices=characteristic_type_choices,
        blank=False,
        null=False,
    )

    requirement = models.CharField(
        max_length=MAX_LENGTH_LONG,
        blank=True,
        null=True,
    )

    # with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'photo',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.code) < self.MIN_LENGTH:
            raise ValidationError('Code must be longer than 3 characters!')

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
