from django import forms
from django.utils import translation

from erp_demo.organization_mng.models import Organization


LABELS_EN = {
    'name': 'Organization Name',
    'attachment': 'Organization logo (Choose file)',
    'eik': 'EIK',
    'mol': 'MOL',
    'address': 'Management full address',
    'manager_name': 'Manager first and last name',
}

LABELS_BG = {
    'name': 'Наименование',
    'attachment': 'Лого на организацията',
    'eik': 'ЕИК',
    'mol': 'МОЛ',
    'address': 'Адрес на управление',
    'manager_name': 'Имена на ръководителя',
}


class OrgFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']

            try:
                self.fields['attachment'].label = LABELS_BG['attachment']
            except KeyError:
                pass

            self.fields['eik'].label = LABELS_BG['eik']
            self.fields['mol'].label = LABELS_BG['mol']
            self.fields['address'].label = LABELS_BG['address']
            self.fields['manager_name'].label = LABELS_BG['manager_name']


class OrgForm(forms.ModelForm, OrgFormMixin):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'attachment': forms.ClearableFileInput(
                attrs={
                    'class': 'file-input',
                    'accept': 'image/*',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class OrgEditForm(forms.ModelForm, OrgFormMixin):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class OrgDeleteForm(forms.ModelForm, OrgFormMixin):
    class Meta:
        model = Organization
        exclude = ['slug', 'attachment']

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


class OrgViewForm(forms.ModelForm, OrgFormMixin):
    class Meta:
        model = Organization
        exclude = ['slug', 'attachment']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
