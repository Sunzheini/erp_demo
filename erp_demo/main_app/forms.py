from django import forms

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


class ManageDbForm(forms.Form):

    select_file = forms.FileField(
        label='',
    )
