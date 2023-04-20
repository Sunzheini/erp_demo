from django import forms

from erp_demo.organization_mng.models import Organization

LABELS = {
    'name': 'Наименование',
    'attachment': 'Лого на организацията',
    'eik': 'ЕИК',
    'mol': 'МОЛ',
    'address': 'Адрес на управление',
    'manager_name': 'Имена на ръководителя',
}

class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = LABELS

        widgets = {
            'attachment': forms.ClearableFileInput(
                attrs={
                    'class': 'file-input',
                    'accept': 'image/*',
                }
            ),
        }

class OrgEditForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = LABELS


class OrgDeleteForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug', 'attachment']

        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class OrgViewForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug', 'attachment']

        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
