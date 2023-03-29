from django import forms

from erp_demo.organization_mng.models import Organization


class CreateOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

        labels = {
            'name': 'Наименование',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'address': 'Адрес на управление',
            'manager_name': 'Имена на ръководителя',
        }
