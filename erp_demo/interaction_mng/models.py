from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.dox_mng.models import Document
from erp_demo.process_mng.models import ProcessStep


class Interaction(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    # many-to-one
    from_process_step = models.ForeignKey(
        ProcessStep,              # which is the related table
        related_name="from_process_step",
        on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        blank=True, null=True,
    )

    # many-to-one
    to_process_step = models.ForeignKey(
        ProcessStep,              # which is the related table
        related_name="to_process_step",
        on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        blank=True, null=True,
    )

    # many-to-many
    documents = models.ManyToManyField(
        Document,
        blank=True,
        through='InteractionToDocuments',
        # doesn't auto create a table but uses the one specified
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def get_related_documents(self):
        return InteractionToDocuments.objects.filter(interaction_id=self.pk)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class InteractionToDocuments(models.Model):
    interaction_id = models.ForeignKey(
        Interaction,
        on_delete=models.CASCADE,
    )
    document_id = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.document_id}"
