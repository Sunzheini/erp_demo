from django import forms
from erp_demo.dox_mng.models import Document
from erp_demo.custom_logic.custom_collections import document_types


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


# ----------------------------------------------------------------------

class DocumentForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    pass


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


class DocumentDeleteForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    class Meta:
        model = Document
        exclude = ['slug', 'status', 'likes', 'is_liked_by_user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    DOCUMENT_TYPES = document_types

    document_type_dropdown = forms.ChoiceField(
        label='Select document type',
        choices=DOCUMENT_TYPES
    )
