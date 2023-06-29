from django.db import models
from django.utils.text import slugify

from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


characteristic_type_choices = [
    ('Product', 'Product'),
    ('Process', 'Process'),
]


class Characteristic(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False,
        null=False,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
    )

    type = models.CharField(
        max_length=50,
        choices=characteristic_type_choices,
        blank=False,
        null=False,
    )

    requirement = models.CharField(
        max_length=199,
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
