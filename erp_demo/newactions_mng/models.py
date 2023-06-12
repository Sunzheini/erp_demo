from django.db import models
from django.utils.text import slugify

from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica


STATUS_CHOICES_EN = (
    ('Not Started', 'Not Started'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
)


class NewAction(models.Model):
    class Meta:
        ordering = ['id']

    scope = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    # description of the action itself
    name = models.CharField(
        max_length=50,
        blank=False, null=False,
        unique=True,
    )

    # # many-to-one
    responsible = models.ForeignKey(
        Employee,
        to_field="identification",
        db_column="owner_ident",
        on_delete=models.CASCADE,
        related_name="responsible",
    )

    target_date = models.DateField(
        blank=False, null=False,
    )

    comments = models.TextField(
        blank=True, null=True,
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES_EN,
        blank=False, null=False,
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[:30])}")
        return super().save(*args, **kwargs)
