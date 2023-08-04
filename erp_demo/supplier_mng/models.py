from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.nonconformity_mng.models import Nonconformity


class Supplier(models.Model):
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

    description = models.TextField(
        blank=True, null=True,
    )

    # many-to-many
    claims = models.ManyToManyField(
        Nonconformity,
        blank=True,
        through='SuppliersToClaims',
        # doesn't auto create a table but uses the one specified
    )

    score = models.IntegerField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def get_related_claims(self):
        try:
            result = SuppliersToClaims.objects.filter(supplier_id=self.pk)
        except SuppliersToClaims.DoesNotExist:
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


class SuppliersToClaims(models.Model):
    supplier_id = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
    )
    claim_id = models.ForeignKey(
        Nonconformity,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.claim_id}"
