from django import forms

from erp_demo.organization_mng.models import Organization


class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = {
            'name': 'Наименование',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'address': 'Адрес на управление',
            'manager_name': 'Имена на ръководителя',
        }


class OrgEditForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = {
            'name': 'Наименование',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'address': 'Адрес на управление',
            'manager_name': 'Имена на ръководителя',
        }


class OrgDeleteForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['slug']

        labels = {
            'name': 'Наименование',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'address': 'Адрес на управление',
            'manager_name': 'Имена на ръководителя',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
