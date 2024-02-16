from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.hr_mng.models import Positions
from erp_demo.maintenance_mng.models import Machine
from erp_demo.supplier_mng.models import Material


class Analysis(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=199,
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

    measurement_unit = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )

    materials = models.ManyToManyField(Material, blank=True)

    work_force = models.ManyToManyField(Positions, blank=True)

    machines = models.ManyToManyField(Machine, blank=True)

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")

        return super().save(*args, **kwargs)
