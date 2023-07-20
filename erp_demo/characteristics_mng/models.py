from django.db import models
from django.utils.text import slugify

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

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )

    code = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False,
        null=False,
        unique=True,
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
