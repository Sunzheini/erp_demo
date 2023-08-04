from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.dox_mng.models import Document
from erp_demo.process_mng.models import ProcessStep


class Interaction(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    # many-to-one
    from_process_step = models.ForeignKey(
        ProcessStep,              # which is the related table
        related_name="from_process_step",
        # on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,
        blank=True,
    )

    # many-to-one
    to_process_step = models.ForeignKey(
        ProcessStep,              # which is the related table
        related_name="to_process_step",
        # on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,
        blank=True,
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

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def get_related_documents(self):
        try:
            result = InteractionToDocuments.objects.filter(interaction_id=self.pk)
        except InteractionToDocuments.DoesNotExist:
            result = None
        return result

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")

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
