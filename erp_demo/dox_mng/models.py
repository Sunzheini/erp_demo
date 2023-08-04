from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MinValueValidator

from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica


UserModel = get_user_model()

TYPE_CHOICES_EN = (
    ('External', 'External'),
    ('Policy', 'Policy'),
    ('Manual', 'Manual'),
    ('Procedure', 'Procedure'),
    ('Instruction', 'Instruction'),
    ('Form', 'Form'),
)

STATUS_CHOICES_EN = (
    ('Latest rev', 'Latest rev'),
    ('Under rev', 'Under rev'),
)


class Document(models.Model):
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        # choices=(
        #     ('Manual', 'Manual'),
        #     ('Procedure', 'Procedure'),
        #     ('Instruction', 'Instruction'),
        #     ('Form', 'Form'),
        # ),
        choices=TYPE_CHOICES_EN,
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    revision = models.PositiveIntegerField(
        blank=False, null=False,
        validators=(
            MinValueValidator(1),
        )
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
        max_length=MAX_LENGTH_SHORT,
        # choices=(
        #     # ('Submitted', 'Submitted'),
        #     # ('Rejected', 'Rejected'),
        #     # ('Approved', 'Approved'),
        # ),

        # choices=(
        #     ('Latest rev', 'Latest rev'),
        #     ('Under rev', 'Under rev'),
        # ),

        choices=STATUS_CHOICES_EN,
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
        # on_delete=models.CASCADE,  # when employee is deleted, delete related documents
        on_delete=models.SET_NULL, null=True,   # set null when process is deleted
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

    # many-to-many
    likes = models.ManyToManyField(
        UserModel,
        blank=True,
        through='DocumentLikesToUsers',
        # doesn't auto create a table but uses the one specified
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.number) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Number must be longer than 1 character!')

        if self.revision < 1:
            raise ValidationError('Revision must be a positive number!')

    def full_document_info(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner is: {self.owner}"

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


class DocumentLikesToUsers(models.Model):
    document_id = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.document_id}, {self.user}"


# Purgatories
# -------------------------------------------------------------------

class DocumentEditPurgatory(models.Model):
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        # choices=(
        #     ('Manual', 'Manual'),
        #     ('Procedure', 'Procedure'),
        #     ('Instruction', 'Instruction'),
        #     ('Form', 'Form'),
        # ),
        choices=TYPE_CHOICES_EN,
        blank=False, null=False,
    )

    number = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    revision = models.PositiveIntegerField(
        blank=False, null=False,
        validators=(
            MinValueValidator(1),
        )
    )

    creation_date = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )

    revision_date = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )

    revision_details = models.TextField(
        blank=True, null=True,
    )

    status = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        # choices=(
        #     ('Latest rev', 'Latest rev'),
        #     ('Under rev', 'Under rev'),
        # ),
        choices=STATUS_CHOICES_EN,
        blank=False, null=False,
    )

    # # many-to-one
    owner = models.ForeignKey(
        Employee,  # which is the related table
        to_field="identification",
        db_column="owner_ident",
        # on_delete=models.CASCADE,  # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,   # set null when process is deleted
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

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.number) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Number must be longer than 1 character!')

        if self.revision < 1:
            raise ValidationError('Revision must be a positive number!')

    def full_document_info(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner: {self.owner}"

    def __str__(self):
        return f"{self.name}, rev.: {self.revision}, " \
               f"owner is: {self.owner}"

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
