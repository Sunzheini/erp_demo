from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.characteristics_mng.models import Characteristic


class DefectCatalogue(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3

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

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def get_related_characteristics(self):
        try:
            result = DefectCatalogueToCharacteristics.objects.filter(defect_catalogue_id=self.pk)
        except DefectCatalogueToCharacteristics.DoesNotExist:
            result = None
        return result

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
