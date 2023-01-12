from django.db import models
from django.utils.text import slugify


class Employee(models.Model):

    class Meta:
        ordering = ['id']

    first_name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    last_name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    identification = models.PositiveIntegerField(
        blank=False, null=False,
    )

    position = models.CharField(
        max_length=30,
        choices=(
            ('Quality Manager', 'Quality Manager'),
            ('Quality Engineer', 'Quality Engineer'),
            ('Quality Inspector', 'Quality Inspector'),
        ),
        blank=False, null=False,
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Name: {self.get_full_name}, " \
               f"ID: {self.identification}, Position: {self.position}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.get_full_name}")
        return super().save(*args, **kwargs)
