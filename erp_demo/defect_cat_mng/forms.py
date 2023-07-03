from django import forms
from django.utils import translation

from erp_demo.defect_cat_mng.models import DefectCatalogue


DEFECT_CATALOGUE_LABELS_EN = {
    'name': 'Name',
    'number': 'Number',
    'description': 'Description',
    'characteristics': 'Characteristics',
}

DEFECT_CATALOGUE_LABELS_BG = {
    'name': 'Име',
    'number': 'Номер',
    'description': 'Описание',
    'characteristics': 'Характеристики',
}


class DefectCatalogueMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = DEFECT_CATALOGUE_LABELS_BG['name']
            self.fields['number'].label = DEFECT_CATALOGUE_LABELS_BG['number']
            self.fields['description'].label = DEFECT_CATALOGUE_LABELS_BG['description']
            self.fields['characteristics'].label = DEFECT_CATALOGUE_LABELS_BG['characteristics']


class DefectCatalogueForm(DefectCatalogueMixin, forms.ModelForm):
    class Meta:
        model = DefectCatalogue
        fields = '__all__'

        labels = DEFECT_CATALOGUE_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class DefectCatalogueEditForm(DefectCatalogueMixin, forms.ModelForm):
    class Meta:
        model = DefectCatalogue
        fields = '__all__'

        labels = DEFECT_CATALOGUE_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class DefectCatalogueDeleteForm(DefectCatalogueMixin, forms.ModelForm):
    class Meta:
        model = DefectCatalogue
        fields = '__all__'

        labels = DEFECT_CATALOGUE_LABELS_EN

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
