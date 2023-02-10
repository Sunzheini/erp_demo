from django import forms

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from erp_demo.main_app.models import Requirements


class ManageDbHRForm(forms.Form):

    select_file = forms.FileField(
        label='',
    )


class ManageDbAllForm(forms.Form):

    select_file = forms.FileField(
        label='',
    )


class DeleteDatabaseForm(forms.Form):
    pass


class RequirementsForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = '__all__'


class RequirementsEditForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = '__all__'


class RequirementsDeleteForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
