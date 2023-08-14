from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MinValueValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.hr_mng.models import Employee
from erp_demo.newactions_mng.models import NewAction


class ActionPlan(models.Model):
    MAX_NAME_LENGTH = 99
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=False, null=False,
        unique=True,
        # added
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    description = models.TextField(
        blank=True, null=True,
    )

    owner = models.ForeignKey(
        Employee,
        blank=True,
        to_field='id',
        db_column="employee_id",
        on_delete=models.SET_NULL, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    # added
    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def get_all_steps(self):
        try:
            result = ActionPlanStep.objects.filter(parent_action_plan_id=self.pk)
        except ActionPlanStep.DoesNotExist:
            result = None
        return result

    @property
    def count_all_steps(self):
        try:
            result = ActionPlanStep.objects.filter(parent_action_plan_id=self.pk).count()
        except ActionPlanStep.DoesNotExist:
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


class ActionPlanStep(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3

    class Meta:
        ordering = ['number']

    number = models.PositiveIntegerField(
        blank=False, null=False,
        # added
        validators=(
            MinValueValidator(1),
        )
    )

    scope = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    # Open Issue
    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        )
    )

    # many-to-one
    parent_action_plan = models.ForeignKey(
        ActionPlan,
        to_field="id",
        db_column="parent_action_plan_id",
        on_delete=models.SET_NULL, null=True,
    )

    actions = models.ManyToManyField(
        NewAction,
        related_name='actions',
        blank=True,
        through='ActionPlanStepToActions',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    # added
    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if self.number < 1:
            raise ValidationError('Number must be greater than 0!')

    @property
    def get_related_actions(self):
        # current code in try and also added except
        try:
            result = ActionPlanStepToActions.objects.filter(action_plan_step_id=self.pk)
        except ActionPlanStepToActions.DoesNotExist:
            result = None
        return result

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")

        # current code in try and also added except
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


class ActionPlanStepToActions(models.Model):
    action_plan_step_id = models.ForeignKey(
        ActionPlanStep,
        on_delete=models.CASCADE,
    )
    action_id = models.ForeignKey(
        NewAction,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.action_id}"
