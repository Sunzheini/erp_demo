from django.db import models
from django.utils.text import slugify

from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica


class Process(models.Model):

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        choices=(
            ('Managerial', 'Managerial'),
            ('Operational', 'Operational'),
            ('Support', 'Support'),
        ),
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=3,
        blank=False, null=False,
        unique=True,
    )

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
        unique=True,
    )

    process_owner = models.ForeignKey(
        Employee,
        to_field="identification",
        db_column="responsible_ident",
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            # self.slug = slugify(f"{self.number}-{self.type}")
            self.slug = slugify(f"{translate_to_maimunica(self.name)}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} {self.name}, Type: {self.type}, PK: {self.pk}"


class ProcessStep(models.Model):

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        choices=(
            ('Terminator', 'Terminator'),
            ('Process', 'Process'),
            ('Decision', 'Decision'),
        ),
        blank=False, null=False,
    )

    number = models.PositiveIntegerField(
        blank=False, null=False,
    )

    name = models.CharField(
        max_length=199,
        blank=False, null=False,
        unique=True,
    )

    # many-to-one
    parent_process = models.ForeignKey(
        Process,                    # which is the related table
        to_field="number",
        db_column="parent_process_number",
        on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        # on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

    # many-to-many
    documents = models.ManyToManyField(
        Document,
        blank=True,
        through='ProcessStepToDocuments',
        # doesn't auto create a table but uses the one specified
    )

    description = models.TextField(
        blank=True, null=True,
    )

    responsible = models.ForeignKey(
        Employee,
        to_field="identification",
        db_column="responsible_ident",
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            # self.slug = slugify(f"{self.name[0:11]}")
            # self.slug = slugify(f"{self.parent_process.number}-{self.number}")
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:50])}")
        return super().save(*args, **kwargs)

    @property
    def get_related_documents(self):
        # return ', '.join([str(f) for f in ProcessStepToDocuments.objects.filter(process_step_id=self.pk)])
        return ProcessStepToDocuments.objects.filter(process_step_id=self.pk)

    def __str__(self):
        # return f"step {self.number} {self.name}, Type: {self.type}, Dox: {self.get_related_documents}"
        return f"{self.parent_process.number},  " \
               f"step: {self.number} {self.name[0:70]}"


class ProcessStepToDocuments(models.Model):
    process_step_id = models.ForeignKey(
        ProcessStep,
        on_delete=models.CASCADE,
    )
    document_id = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.document_id}"
