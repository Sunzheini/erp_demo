from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MinValueValidator

from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


class Organization(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

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

    # with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'photo',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

    eik = models.PositiveIntegerField(
        blank=False, null=False,
        validators=(
            MinValueValidator(MIN_SHORT_LENGTH),
        ),
    )

    mol = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    address = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    manager_name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.mol) < self.MIN_LENGTH:
            raise ValidationError('MOL must be longer than 3 characters!')

        if len(self.address) < self.MIN_LENGTH:
            raise ValidationError('Address must be longer than 3 characters!')

        if len(self.manager_name) < self.MIN_LENGTH:
            raise ValidationError('Manager name must be longer than 3 characters!')

        if len(str(self.eik)) < self.MIN_SHORT_LENGTH:
            raise ValidationError('EIK must be longer than 1 character!')

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
