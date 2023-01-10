from django.db import models

from erp_demo.dox_mng.models import Document


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

    name = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )

    def __str__(self):
        return f"Process {self.pk} / Type: {self.type} / Name: {self.name}"


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

    name = models.CharField(
        max_length=31,
        blank=False, null=False,
        unique=True,
    )

    # many-to-one
    parent_process = models.ForeignKey(
        Process,                    # which is the related table
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

    @property
    def get_related_documents(self):
        return ', '.join([str(f) for f in ProcessStepToDocuments.objects.filter(process_step_id=self.pk)])

    def __str__(self):
        return f"Process Step {self.pk} / Type: {self.type} " \
               f"/ Name: {self.name} / " \
               f"Parent: {self.parent_process.pk} " \
               f"- {self.parent_process.name} / " \
               f"Documents: {self.get_related_documents}"


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
