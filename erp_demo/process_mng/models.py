from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MinValueValidator

from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.kpi_mng.models import Kpi
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.risk_mng.models import Risk


PROCESS_CHOICES_EN=(
    ('Managerial', 'Managerial'),
    ('Operational', 'Operational'),
    ('Support', 'Support'),
)

PROCESS_STEP_CHOICES_EN=(
    ('Terminator', 'Terminator'),
    ('Process', 'Process'),
    ('Decision', 'Decision'),
)


class Process(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_TYPE = 30
    MAX_LENGTH_NUMBER = 3
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        # choices=(
        #     ('Managerial', 'Managerial'),
        #     ('Operational', 'Operational'),
        #     ('Support', 'Support'),
        # ),
        choices=PROCESS_CHOICES_EN,
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=MAX_LENGTH_NUMBER,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    process_owner = models.ForeignKey(
        Employee,
        to_field="identification",
        db_column="responsible_ident",
        # on_delete=models.CASCADE,
        on_delete=models.SET_NULL, null=True,
    )

    # many-to-many
    kpis = models.ManyToManyField(
        Kpi,
        blank=True,
        through='ProcessToKpis',
        # doesn't auto create a table but uses the one specified
    )

    opportunities = models.ManyToManyField(
        Opportunity,
        blank=True,
        through='ProcessToOpportunities',
    )

    risks = models.ManyToManyField(
        Risk,
        blank=True,
        through='ProcessToRisks',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.number) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Number must be longer than 1 character!')

    @property
    def get_related_kpis(self):
        try:
            result = ProcessToKpis.objects.filter(process_id=self.pk)
        except ProcessToKpis.DoesNotExist:
            result = None
        return result

    @property
    def get_related_opportunities(self):
        try:
            result = ProcessToOpportunities.objects.filter(process_id=self.pk)
        except ProcessToOpportunities.DoesNotExist:
            result = None
        return result

    @property
    def get_related_risks(self):
        try:
            result = ProcessToRisks.objects.filter(process_id=self.pk)
        except ProcessToRisks.DoesNotExist:
            result = None
        return result

    @property
    def count_related_kpis(self):
        return self.get_related_kpis.count()

    @property
    def count_related_opportunities(self):
        return self.get_related_opportunities.count()

    @property
    def count_related_risks(self):
        return self.get_related_risks.count()

    @property
    def list_of_process_types(self):
        return [x[0] for x in self._meta.get_field('type').choices]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:50])}")

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
        return f"{self.number} {self.name}, Type: {self.type}, PK: {self.pk}"


class ProcessStep(models.Model):
    MAX_LENGTH_LONG = 199
    MAX_LENGTH_SHORT = 30
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        # choices=(
        #     ('Terminator', 'Terminator'),
        #     ('Process', 'Process'),
        #     ('Decision', 'Decision'),
        # ),
        choices=PROCESS_STEP_CHOICES_EN,
        blank=False, null=False,
    )

    number = models.PositiveIntegerField(
        blank=False, null=False,
        validators=(
            MinValueValidator(MIN_SHORT_LENGTH),
        )
    )

    name = models.CharField(
        max_length=MAX_LENGTH_LONG,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    # many-to-one
    parent_process = models.ForeignKey(
        Process,                    # which is the related table
        to_field="number",
        db_column="parent_process_number",
        # on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,   # set null when process is deleted
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
        # on_delete=models.CASCADE,
        on_delete=models.SET_NULL, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if self.number < self.MIN_SHORT_LENGTH:
            raise ValidationError('Number must be longer than 1 character!')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:50])}")

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

    @property
    def get_related_documents(self):
        # return ', '.join([str(f) for f in ProcessStepToDocuments.objects.filter(process_step_id=self.pk)])
        try:
            result = ProcessStepToDocuments.objects.filter(process_step_id=self.pk)
        except ProcessStepToDocuments.DoesNotExist:
            result = None
        return result

    def __str__(self):
        # return f"step {self.number} {self.name}, Type: {self.type}, Dox: {self.get_related_documents}"
        # return f"{self.parent_process.number},  " \
        #        f"step: {self.number} {self.name[0:70]}"
        return f"{self.parent_process.number}, {self.number}. {self.name[0:70]}..."


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


class ProcessToKpis(models.Model):
    process_id = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
    )
    kpi_id = models.ForeignKey(
        Kpi,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.kpi_id}"


class ProcessToOpportunities(models.Model):
    process_id = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
    )
    opportunity_id = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.opportunity_id}"


class ProcessToRisks(models.Model):
    process_id = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
    )
    risk_id = models.ForeignKey(
        Risk,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.risk_id}"
