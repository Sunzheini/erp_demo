from django import forms
from django.utils import translation

from erp_demo.custom_logic.custom_collections import search_types_en, search_types_bg
from erp_demo.main_app.models import Requirements


LABELS_EN = {
    'organization': 'Organization',
    'external_document': 'External document',
    'clause': 'Clause',
    'clause_name': 'Clause name',
    'description': 'Description',
    'covered_by_process_step': 'Covered by process step',
}

LABELS_BG = {
    'organization': 'Организация',
    'external_document': 'Външен документ',
    'clause': 'Клауза',
    'clause_name': 'Име клауза',
    'description': 'Описание',
    'covered_by_process_step': 'Покритo от процесна стъпка',
}


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


class ExportDatabaseForm(forms.Form):
    pass


class RequirementsMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['organization'].label = LABELS_BG['organization']
            self.fields['external_document'].label = LABELS_BG['external_document']
            self.fields['clause'].label = LABELS_BG['clause']
            self.fields['clause_name'].label = LABELS_BG['clause_name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['covered_by_process_step'].label = LABELS_BG['covered_by_process_step']


class RequirementsForm(forms.ModelForm, RequirementsMixin):
    class Meta:
        model = Requirements
        fields = '__all__'

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class RequirementsEditForm(forms.ModelForm, RequirementsMixin):
    class Meta:
        model = Requirements
        fields = '__all__'

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class RequirementsDeleteForm(forms.ModelForm, RequirementsMixin):
    class Meta:
        model = Requirements
        fields = '__all__'

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


class SearchForm(forms.Form):
    SEARCH_TYPES = search_types_en

    form_keyword = forms.CharField(
        max_length=30,
        label='Enter keyword',
    )

    search_type_dropdown = forms.ChoiceField(
        label='Search categories',
        choices=SEARCH_TYPES,
        initial='All',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['form_keyword'].label = 'Kлючова дума'
            self.fields['search_type_dropdown'].label = 'Категории'
            self.fields['search_type_dropdown'].choices = search_types_bg

# ----------------------------------------------------------------------

class RequirementsDocumentForm(forms.Form):
    requirements_document_dropdown = forms.ChoiceField(
        label='Requirements document',
        choices=(('All', 'All'),),
    )

    # get a tuple suitable for 'choices' from a table
    @staticmethod
    def requirements_documents():
        all_ext_documents = Requirements.objects.values_list('external_document', flat=True)
        all_ext_documents = list(set(all_ext_documents))
        ext_documents_tuples = [(item, item) for item in all_ext_documents]
        result = tuple(ext_documents_tuples)
        result = (('All', 'All'),) + result
        return result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['requirements_document_dropdown'].label = 'Документ с изисквания'

        self.fields['requirements_document_dropdown'].choices = self.requirements_documents()
