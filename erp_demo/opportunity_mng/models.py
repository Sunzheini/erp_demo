from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.newactions_mng.models import NewAction


class Opportunity(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    long_term_action = models.ManyToManyField(
        NewAction,
        blank=True,
        through='OpportunitiesToActions',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def get_related_actions(self):
        return OpportunitiesToActions.objects.filter(opportunity_id=self.id)

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class OpportunitiesToActions(models.Model):
    opportunity_id = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
    )
    action_id = models.ForeignKey(
        NewAction,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.action_id}"
