import os
from django import forms
from erp_demo.dox_mng.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentDeleteForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['attachment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        doc_path = self.instance.attachment.path    # attachment is a field in the model
        self.instance.delete()
        os.remove(doc_path)
        return self.instance

