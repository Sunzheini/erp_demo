from django import forms

from erp_demo.custom_logic.custom_collections import search_types
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


class SearchForm(forms.Form):
    SEARCH_TYPES = search_types

    form_keyword = forms.CharField(
        max_length=30,
        label='Enter keyword',
    )

    search_type_dropdown = forms.ChoiceField(
        label='Search categories',
        choices=SEARCH_TYPES,
        initial='All',
    )
