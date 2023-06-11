from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica


TYPE_CHOICES_EN = (
    ('Containment', 'Containment'),
    ('Correction', 'Correction'),
    ('Corrective Action', 'Corrective Action'),
    ('Systematic Action', 'Systematic Action'),
    ('Improvement', 'Improvement'),
    ('Task', 'Task'),
)

STATUS_CHOICES_EN = (
    ('Not Defined', 'Not Defined'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
)


class Action(models.Model):
    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES_EN,
        blank=False, null=False,
    )

    scope = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    # open issue: nonc (to rootcause?), risk, improvement, etc. object
    # ------------------------------------------------------------------------------------------------

    # the following three fields are for generic relations (they can't be used in ForeignKey or ManyToMany relationships)

    # information about the model that your instance is related to
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    # will store the id of the related object
    object_id = models.PositiveIntegerField(null=True, blank=True)
    # will allow you to retrieve the related object
    content_object = GenericForeignKey('content_type', 'object_id')

    # ------------------------------------------------------------------------------------------------

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
