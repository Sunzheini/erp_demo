import os
from django import forms
from erp_demo.dox_mng.models import Document
from erp_demo.main_app.custom_collections import document_types


class DocumentModelAndExcludeMixin:
    class Meta:
        model = Document
        exclude = ['slug']


# ----------------------------------------------------------------------

class DocumentForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    pass


class DocumentEditForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    pass


class DocumentDeleteForm(forms.ModelForm, DocumentModelAndExcludeMixin):
    class Meta:
        model = Document
        exclude = ['slug']

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
        choices=DOCUMENT_TYPES,
    )
