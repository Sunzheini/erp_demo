from django.db import models
from django.utils.text import slugify
from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


class Organization(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
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
    )

    mol = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    address = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    manager_name = models.CharField(
        max_length=MAX_LENGTH,
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
