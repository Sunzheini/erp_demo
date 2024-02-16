from django import forms
from django.utils import translation

from erp_demo.supplier_mng.models import Supplier, Material

LABELS_EN = {
    'name': 'Supplier name',
    'description': 'Description',
    'claims': 'Claims',
    'score': 'Score',
}

LABELS_BG = {
    'name': 'Име на доставчик',
    'description': 'Описание',
    'claims': 'Рекламации',
    'score': 'Рейтинг',
}

MATERIAL_LABELS_EN = {
    'name': 'Material name',
    'description': 'Description',
    'quantity': 'Quantity',
    'measurement_unit': 'Measurement unit',
    'price_per_unit': 'Price per unit',
}

MATERIAL_LABELS_BG = {
    'name': 'Име на материал',
    'description': 'Описание',
    'quantity': 'Количество',
    'measurement_unit': 'Мерна единица',
    'price_per_unit': 'Цена на единица',
}


class SupplierFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['claims'].label = LABELS_BG['claims']
            self.fields['score'].label = LABELS_BG['score']


class MaterialFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = MATERIAL_LABELS_BG['name']
            self.fields['description'].label = MATERIAL_LABELS_BG['description']
            self.fields['quantity'].label = MATERIAL_LABELS_BG['quantity']
            self.fields['measurement_unit'].label = MATERIAL_LABELS_BG['measurement_unit']
            self.fields['price_per_unit'].label = MATERIAL_LABELS_BG['price_per_unit']


class SupplierForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class SupplierEditForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class SupplierDeleteForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

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


class SupplierViewForm(forms.ModelForm, SupplierFormMixin):
    class Meta:
        model = Supplier
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class MaterialForm(forms.ModelForm, MaterialFormMixin):
    class Meta:
        model = Material
        exclude = ['slug']

        labels = MATERIAL_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class MaterialEditForm(forms.ModelForm, MaterialFormMixin):
    class Meta:
        model = Material
        exclude = ['slug']

        labels = MATERIAL_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class MaterialDeleteForm(forms.ModelForm, MaterialFormMixin):
    class Meta:
        model = Material
        exclude = ['slug']

        labels = MATERIAL_LABELS_EN

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


class MaterialViewForm(forms.ModelForm, MaterialFormMixin):
    class Meta:
        model = Material
        exclude = ['slug']

        labels = MATERIAL_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
