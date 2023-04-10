from django.db import models
from django.utils.text import slugify

from erp_demo.main_app.translator import translate_to_maimunica


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

    mol = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    correspondence_address = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    contact_person = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    phone = models.CharField(
        max_length=20,
        blank=False, null=False,
    )

    email = models.EmailField(
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
