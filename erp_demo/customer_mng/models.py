from django.db import models
from django.utils.text import slugify
from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


class Customer(models.Model):
    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        choices=(
            ('', 'Празно'),
            ('Физическо лице', 'Физическо лице'),
            ('Юридическо лице', 'Юридическо лице'),
            ('Институция', 'Институция'),
        ),
        blank=False, null=False,
    )

    # with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'photo',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    registration_address = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    registration_city = models.CharField(
        max_length=50,
        blank=False, null=False,
    )

    eik = models.PositiveIntegerField(
        blank=True, null=True,
    )

    mol1 = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    mol2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    mol3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    mol4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    mol5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    correspondence_address1 = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    correspondence_address2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    correspondence_address3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    correspondence_address4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    correspondence_address5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    contact_person1 = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    contact_person2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    contact_person3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    contact_person4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    contact_person5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    phone1 = models.CharField(
        max_length=20,
        blank=False, null=False,
    )

    phone2 = models.CharField(
        max_length=20,
        blank=True, null=True,
    )

    phone3 = models.CharField(
        max_length=20,
        blank=True, null=True,
    )

    phone4 = models.CharField(
        max_length=20,
        blank=True, null=True,
    )

    phone5 = models.CharField(
        max_length=20,
        blank=True, null=True,
    )

    email1 = models.EmailField(
        blank=False, null=False,
    )

    email2 = models.EmailField(
        blank=True, null=True,
    )

    email3 = models.EmailField(
        blank=True, null=True,
    )

    email4 = models.EmailField(
        blank=True, null=True,
    )

    email5 = models.EmailField(
        blank=True, null=True,
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

    def __str__(self):
        return f"{self.name}"
