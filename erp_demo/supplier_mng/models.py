from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.nonconformity_mng.models import Nonconformity


class Supplier(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
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

    @property
    def get_related_claims(self):
        return SuppliersToClaims.objects.filter(supplier_id=self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

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
