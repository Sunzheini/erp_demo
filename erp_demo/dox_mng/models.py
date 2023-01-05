from cloudinary import models as cloudinary_models
from django.db import models


class Document(models.Model):

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )
    revision = models.PositiveIntegerField(
        blank=False, null=False,
    )
    owner = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

# with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'file',
        resource_type="auto",
        blank=False, null=False,
        use_filename=True,
        unique_filename=False,
    )

# without cloudinary
    # attachment = models.FileField(
    #     blank=False, null=False,
    # )

    slug = models.SlugField(
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"
