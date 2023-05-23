from django import forms
from django.utils import translation

from erp_demo.dox_mng.models import Document
from erp_demo.custom_logic.custom_collections import document_types_en, document_types_bg

LABELS_EN = {
    'type': 'Type',
    'number': 'Number',
    'name': 'Name',
    'revision': 'Revision',
    'creation_date': 'Creation date',
    'revision_date': 'Revision date',
    'revision_details': 'Revision details',
    'owner': 'Owner',
    'attachment': 'Attachment',
}

LABELS_BG = {
    'type': 'Вид',
    'number': 'Номер',
    'name': 'Име',
    'revision': 'Ревизия',
    'creation_date': 'Дата на създаване',
    'revision_date': 'Дата на ревизия',
    'revision_details': 'Детайли на ревизията',
    'owner': 'Собственик',
    'attachment': 'Прикачен файл',
}

TYPE_CHOICES_BG = (
    ('Manual', 'Ръководство'),
    ('Procedure', 'Процедура'),
    ('Instruction', 'Инструкция'),
    ('Form', 'Формуляр'),
)

STATUS_CHOICES_BG = (
    ('Latest rev', 'Последна рев'),
    ('Under rev', 'Под ревизия'),
)

class DocumentModelAndExcludeMixin:
    class Meta:
        model = Document
        exclude = ['slug', 'status', 'likes', 'is_liked_by_user']

        widgets = {
            'creation_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',  # taka veshe izkarva kalendara
                }
            ),
            'revision_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].label = LABELS_BG['type']
            self.fields['type'].choices = TYPE_CHOICES_BG

            self.fields['number'].label = LABELS_BG['number']
            self.fields['name'].label = LABELS_BG['name']
            self.fields['revision'].label = LABELS_BG['revision']
            self.fields['creation_date'].label = LABELS_BG['creation_date']
            self.fields['revision_date'].label = LABELS_BG['revision_date']
            self.fields['revision_details'].label = LABELS_BG['revision_details']
            self.fields['owner'].label = LABELS_BG['owner']

            try:
                self.fields['attachment'].label = LABELS_BG['attachment']
            except KeyError:
                pass

# ----------------------------------------------------------------------

class DocumentForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class DocumentEditForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    class Meta:
        model = Document
        exclude = ['slug', 'status', 'likes', 'is_liked_by_user']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'revision': forms.NumberInput(
                attrs={
                    'readonly': 'readonly',
                }
            ),
            'creation_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',  # taka veshe izkarva kalendara
                }
            ),
            'revision_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class DocumentDeleteForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    class Meta:
        model = Document
        exclude = ['slug', 'status', 'likes', 'is_liked_by_user',
                   'attachment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

# without heroku
    # def save(self, commit=True):
    #     doc_path = self.instance.attachment.path    # attachment is a field in the model
    #     self.instance.delete()
    #     os.remove(doc_path)
    #     return self.instance

# with heroku
    def save(self, commit=True):
        self.instance.delete()
        return self.instance


# ----------------------------------------------------------------------

class DocumentTypeForm(forms.Form):
    DOCUMENT_TYPES = document_types_en

    document_type_dropdown = forms.ChoiceField(
        label='Select document type',
        choices=DOCUMENT_TYPES
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['document_type_dropdown'].label = 'Вид документ'
            self.fields['document_type_dropdown'].choices = document_types_bg
