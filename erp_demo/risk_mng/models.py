from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.newactions_mng.models import NewAction


class Risk(models.Model):
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

    description = models.TextField(
        blank=True, null=True,
    )

    probability = models.IntegerField(
        blank=False, null=False,
    )

    impact = models.IntegerField(
        blank=False, null=False,
    )

    immediate_action = models.TextField(
        blank=True, null=True,
    )

    ia_test_period = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    long_term_action = models.ManyToManyField(
        NewAction,
        blank=True,
        through='RisksToActions',
    )

    new_probability = models.IntegerField(
        blank=True, null=True,
    )

    new_impact = models.IntegerField(
        blank=True, null=True,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def value(self):
        return self.probability * self.impact

    @property
    def get_related_actions(self):
        try:
            result = RisksToActions.objects.filter(risk_id=self.pk)
        except RisksToActions.DoesNotExist:
            result = None
        return result

    @property
    def new_value(self):
        if self.new_probability is None or self.new_impact is None:
            return None
        return self.new_probability * self.new_impact

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

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


class RisksToActions(models.Model):
    risk_id = models.ForeignKey(
        Risk,
        on_delete=models.CASCADE,
    )
    action_id = models.ForeignKey(
        NewAction,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.action_id}"
