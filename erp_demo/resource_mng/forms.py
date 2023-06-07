from django import forms
from django.utils import translation

from erp_demo.resource_mng.models import Resource, ResourcesAssignedToEmployees, ResourcesAssignedToProcess

LABELS_EN = {
    'name': 'Resource name',
    'description': 'Description',
    'quantity': 'Quantity',
}

LABELS_BG = {
    'name': 'Име на ресурс',
    'description': 'Описание',
    'quantity': 'Количество',
}

LABELS_EN_ASSIGN = {
    'employee': 'Employee',
    'resource': 'Resource',
    'quantity': 'Quantity',
}

LABELS_BG_ASSIGN = {
    'employee': 'Служител',
    'resource': 'Ресурс',
    'quantity': 'Количество',
}


LABELS_EN_ASSIGN2 = {
    'process': 'Process',
    'resource': 'Resource',
    'quantity': 'Quantity',
}


LABELS_BG_ASSIGN2 = {
    'process': 'Процес',
    'resource': 'Ресурс',
    'quantity': 'Количество',
}


class ResourceFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['quantity'].label = LABELS_BG['quantity']


class ResourceAssignToEmployeeFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['employee'].label = LABELS_BG_ASSIGN['employee']
            self.fields['resource'].label = LABELS_BG_ASSIGN['resource']
            self.fields['quantity'].label = LABELS_BG_ASSIGN['quantity']


class ResourceAssignToProcessFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['process'].label = LABELS_BG_ASSIGN2['process']
            self.fields['resource'].label = LABELS_BG_ASSIGN2['resource']
            self.fields['quantity'].label = LABELS_BG_ASSIGN2['quantity']


class ResourceForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ResourceEditForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ResourceDeleteForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
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


class ResourceViewForm(forms.ModelForm, ResourceFormMixin):
    class Meta:
        model = Resource
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class ResourceAssignToEmployeeForm(forms.ModelForm, ResourceAssignToEmployeeFormMixin):
    class Meta:
        model = ResourcesAssignedToEmployees
        exclude = ['slug']

        labels = LABELS_EN_ASSIGN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ResourceAssignToProcessForm(forms.ModelForm, ResourceAssignToProcessFormMixin):
    class Meta:
        model = ResourcesAssignedToProcess
        exclude = ['slug']

        labels = LABELS_EN_ASSIGN2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ChangeForm(forms.Form):
    new_quantity = forms.IntegerField(label='Quantity', min_value=0)
