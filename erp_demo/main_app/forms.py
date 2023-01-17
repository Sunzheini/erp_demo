from django import forms

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


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
