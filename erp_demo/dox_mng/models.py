from cloudinary import models as cloudinary_models
from django.db import models
from django.utils.text import slugify

from erp_demo.hr_mng.models import Employee
from erp_demo.main_app.custom_validators import validate_file_size
from erp_demo.main_app.translator import translate_to_maimunica


class Document(models.Model):
    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        choices=(
            ('Manual', 'Manual'),
            ('Procedure', 'Procedure'),
            ('Instruction', 'Instruction'),
            ('Form', 'Form'),
        ),
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    name = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )

    revision = models.PositiveIntegerField(
        blank=False, null=False,
    )

    creation_date = models.DateField(
        blank=True, null=True,
    )

    revision_date = models.DateField(
        blank=True, null=True,
    )

    revision_details = models.TextField(
        blank=True, null=True,
    )

    status = models.CharField(
        max_length=30,
        choices=(
            ('Submitted', 'Submitted'),
            ('Rejected', 'Rejected'),
            ('Approved', 'Approved'),
        ),
        blank=False, null=False,
    )

    # owner = models.CharField(
    #     max_length=30,
    #     blank=False, null=False,
    # )

    # # many-to-one
    owner = models.ForeignKey(
        Employee,  # which is the related table
        to_field="identification",
        db_column="owner_ident",
        on_delete=models.CASCADE,  # when process is deleted, delete related process steps
        # on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

# with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'file',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

# without cloudinary
    # attachment = models.FileField(
    #     blank=False, null=False,
    #     validators = (validate_file_size,),
    # )

    is_liked_by_user = models.BooleanField(
        default=False,
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def full_document_info(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner is: {self.owner}"

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        if not self.slug:
            # self.slug = slugify(f"{self.name}")
            # self.slug = slugify(f"{self.owner}-{self.type}-{self.revision}")
            self.slug = slugify(f"{translate_to_maimunica(self.name)}")
        return super().save(*args, **kwargs)


# Purgatories
# -------------------------------------------------------------------

class DocumentEditPurgatory(models.Model):
    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        choices=(
            ('Manual', 'Manual'),
            ('Procedure', 'Procedure'),
            ('Instruction', 'Instruction'),
            ('Form', 'Form'),
        ),
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    revision = models.PositiveIntegerField(
        blank=False, null=False,
    )

    creation_date = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    revision_date = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    revision_details = models.TextField(
        blank=True, null=True,
    )

    status = models.CharField(
        max_length=30,
        choices=(
            ('Submitted', 'Submitted'),
            ('Rejected', 'Rejected'),
            ('Approved', 'Approved'),
        ),
        blank=False, null=False,
    )

    # # many-to-one
    owner = models.ForeignKey(
        Employee,  # which is the related table
        to_field="identification",
        db_column="owner_ident",
        on_delete=models.CASCADE,  # when process is deleted, delete related process steps
        # on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

# with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'file',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

# without cloudinary
    # attachment = models.FileField(
    #     blank=False, null=False,
    # )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def full_document_info(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner is: {self.owner}"

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)     # this method saves twice so commented!!!
        if not self.slug:
            # self.slug = slugify(f"{self.name}")
            # self.slug = slugify(f"{self.owner}-{self.type}-{self.revision}")
            self.slug = slugify(f"{translate_to_maimunica(self.name)}")
        return super().save(*args, **kwargs)
