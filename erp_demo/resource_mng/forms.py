from django import forms
from django.utils import translation

from erp_demo.resource_mng.models import Resource


LABELS_EN = {
    'name': 'Resource name',
    'description': 'Description',
    'quantity': 'Quantity',
}

LABELS_BG = {
    'name': 'Име на ресурс',
    'description': 'Описание',
    'quantity': 'Количество',
}


class ResourceFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['quantity'].label = LABELS_BG['quantity']


class ResourceForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ResourceEditForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ResourceDeleteForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class ResourceViewForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
