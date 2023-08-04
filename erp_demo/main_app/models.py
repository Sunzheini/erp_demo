from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.process_mng.models import ProcessStep


class MyTasks(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    number = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )


class CaptainsLog(models.Model):
    MAX_LENGTH_LONG = 297
    MAX_LENGTH_SHORT = 30

    class Meta:
        ordering = ['id']

    operation = models.CharField(
        max_length=MAX_LENGTH_LONG,
        blank=False, null=False,
    )

    performed_at_time = models.DateTimeField(
        blank=False, null=False,
        auto_now_add=True,
    )

    execution_time = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )


class Requirements(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 30
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    organization = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    external_document = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    clause = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    clause_name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    description = models.TextField(
        blank=True, null=True,
    )

    # many-to-many
    covered_by_process_step = models.ManyToManyField(
        ProcessStep,
        blank=True,
        through='RequirementToProcessStep',
        # doesn't auto create a table but uses the one specified
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.organization) < self.MIN_LENGTH:
            raise ValidationError('Organization must be longer than 3 characters!')

        if len(self.external_document) < self.MIN_LENGTH:
            raise ValidationError('External document must be longer than 3 characters!')

        if len(self.clause) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Clause must be longer than 1 character!')

        if len(self.clause_name) < self.MIN_LENGTH:
            raise ValidationError('Clause name must be longer than 3 characters!')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.organization}-"
                                f"{self.clause}-"
                                f"{translate_to_maimunica(self.description[0:20])}")

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
    def get_related_process_steps(self):
        try:
            result = RequirementToProcessStep.objects.filter(requirement_id=self.id)
        except RequirementToProcessStep.DoesNotExist:
            result = None
        return result

    def __str__(self):
        return f"{self.organization}-{self.clause}"


class RequirementToProcessStep(models.Model):
    requirement_id = models.ForeignKey(
        Requirements,
        on_delete=models.CASCADE,
    )
    process_step_id = models.ForeignKey(
        ProcessStep,
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.process_step_id}"


