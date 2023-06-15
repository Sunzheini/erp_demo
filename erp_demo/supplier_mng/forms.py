from django import forms
from django.utils import translation

from erp_demo.supplier_mng.models import Supplier

LABELS_EN = {
    'name': 'Supplier name',
    'description': 'Description',
    'claims': 'Claims',
    'score': 'Score',
}

LABELS_BG = {
    'name': 'Име на доставчик',
    'description': 'Описание',
    'claims': 'Рекламации',
    'score': 'Рейтинг',
}


class SupplierFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['claims'].label = LABELS_BG['claims']
            self.fields['score'].label = LABELS_BG['score']


class SupplierForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class SupplierEditForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class SupplierDeleteForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
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


class SupplierViewForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
