from django import forms
from django.utils import translation

from erp_demo.characteristics_mng.models import Characteristic

LABELS_EN = {
    'name': 'Characteristic',
    'code': 'Code',
    'type': 'Type',
    'requirement': 'Requirement',
    'attachment': 'Attachment',
}

LABELS_BG = {
    'name': 'Характеристика',
    'code': 'Код',
    'type': 'Тип',
    'requirement': 'Изискване',
    'attachment': 'Прложение',
}


class CharacteristicFormMixin:
    def change_labels(self):
        if translation.get_language() == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['code'].label = LABELS_BG['code']
            self.fields['type'].label = LABELS_BG['type']
            self.fields['requirement'].label = LABELS_BG['requirement']
            self.fields['attachment'].label = LABELS_BG['attachment']


class CharacteristicForm(forms.ModelForm, CharacteristicFormMixin):
    class Meta:
        model = Characteristic
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels()


class CharacteristicEditForm(forms.ModelForm, CharacteristicFormMixin):
    class Meta:
        model = Characteristic
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels()


class CharacteristicDeleteForm(forms.ModelForm, CharacteristicFormMixin):
    class Meta:
        model = Characteristic
        exclude = ['slug', 'type', 'attachment']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class CharacteristicViewForm(forms.ModelForm, CharacteristicFormMixin):
    class Meta:
        model = Characteristic
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
