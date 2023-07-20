from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.characteristics_mng.models import Characteristic


class DefectCatalogue(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
    )

    number = models.PositiveIntegerField(
        blank=True, null=True,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    characteristics = models.ManyToManyField(
        Characteristic,
        related_name='characteristics',
        blank=True,
        through='DefectCatalogueToCharacteristics',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def get_related_characteristics(self):
        return DefectCatalogueToCharacteristics.objects.filter(defect_catalogue_id=self.pk)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class DefectCatalogueToCharacteristics(models.Model):
    defect_catalogue_id = models.ForeignKey(
        DefectCatalogue,
        on_delete=models.CASCADE,
    )

    characteristic_id = models.ForeignKey(
        Characteristic,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.characteristic_id}"
