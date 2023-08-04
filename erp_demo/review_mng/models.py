from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.kpi_mng.models import Kpi
from erp_demo.nonconformity_mng.models import Nonconformity
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.resource_mng.models import Resource
from erp_demo.risk_mng.models import Risk
from erp_demo.supplier_mng.models import Supplier


class ManagementReview(models.Model):
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

    date = models.DateField(
        blank=False, null=False,
    )

    status_from_previous_reviews = models.TextField(
        blank=True, null=True,
    )

    external_and_internal_changes = models.TextField(
        blank=True, null=True,
    )

    customer_feedback = models.TextField(
        blank=True, null=True,
    )

    kpis = models.ManyToManyField(
        Kpi,
        related_name='kpis',
        blank=True,
        through='ManagementReviewToKpi',
    )

    kpis_comments = models.TextField(
        blank=True, null=True,
    )

    other_kpis = models.TextField(
        blank=True, null=True,
    )

    nonconformities = models.ManyToManyField(
        Nonconformity,
        related_name='nonconformities',
        blank=True,
        through='ManagementReviewToNonconformity',
    )

    nonconformities_comments = models.TextField(
        blank=True, null=True,
    )

    audit_results = models.TextField(
        blank=True, null=True,
    )

    suppliers = models.ManyToManyField(
        Supplier,
        related_name='suppliers',
        blank=True,
        through='ManagementReviewToSupplier',
    )

    suppliers_comments = models.TextField(
        blank=True, null=True,
    )

    resources = models.ManyToManyField(
        Resource,
        related_name='resources',
        blank=True,
        through='ManagementReviewToResource',
    )

    resources_comments = models.TextField(
        blank=True, null=True,
    )

    risks = models.ManyToManyField(
        Risk,
        related_name='risks',
        blank=True,
        through='ManagementReviewToRisk',
    )

    risks_comments = models.TextField(
        blank=True, null=True,
    )

    opportunities = models.ManyToManyField(
        Opportunity,
        related_name='opportunities',
        blank=True,
        through='ManagementReviewToOpportunity',
    )

    opportunities_comments = models.TextField(
        blank=True, null=True,
    )

    costs_of_poor_quality = models.TextField(
        blank=True, null=True,
    )

    manufacturing_feasibility = models.TextField(
        blank=True, null=True,
    )

    other_topics = models.TextField(
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
    def get_related_kpis(self):
        try:
            result = ManagementReviewToKpi.objects.filter(management_review_id=self.id)
        except ManagementReviewToKpi.DoesNotExist:
            result = None
        return result

    @property
    def get_related_nonconformities(self):
        try:
            result = ManagementReviewToNonconformity.objects.filter(management_review_id=self.id)
        except ManagementReviewToNonconformity.DoesNotExist:
            result = None
        return result

    @property
    def get_related_suppliers(self):
        try:
            result = ManagementReviewToSupplier.objects.filter(management_review_id=self.id)
        except ManagementReviewToSupplier.DoesNotExist:
            result = None
        return result

    @property
    def get_related_resources(self):
        try:
            result = ManagementReviewToResource.objects.filter(management_review_id=self.id)
        except ManagementReviewToResource.DoesNotExist:
            result = None
        return result

    @property
    def get_related_risks(self):
        try:
            result = ManagementReviewToRisk.objects.filter(management_review_id=self.id)
        except ManagementReviewToRisk.DoesNotExist:
            result = None
        return result

    @property
    def get_related_opportunities(self):
        try:
            result = ManagementReviewToOpportunity.objects.filter(management_review_id=self.id)
        except ManagementReviewToOpportunity.DoesNotExist:
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


class ManagementReviewToKpi(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    kpi_id = models.ForeignKey(
        Kpi,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.kpi_id}"


class ManagementReviewToNonconformity(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    nonconformity_id = models.ForeignKey(
        Nonconformity,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.nonconformity_id}"


class ManagementReviewToSupplier(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    supplier_id = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.supplier_id}"


class ManagementReviewToResource(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    resource_id = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.resource_id}"


class ManagementReviewToRisk(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    risk_id = models.ForeignKey(
        Risk,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.risk_id}"


class ManagementReviewToOpportunity(models.Model):
    management_review_id = models.ForeignKey(
        ManagementReview,
        on_delete=models.CASCADE,
    )

    opportunity_id = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.opportunity_id}"

