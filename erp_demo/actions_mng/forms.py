from django import forms
from django.forms import TextInput
from django.utils import translation

from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from erp_demo.actions_mng.models import Action
from erp_demo.nonconformity_mng.models import Nonconformity
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.risk_mng.models import Risk

LABELS_EN = {
    'type': 'Type',
    'scope': 'Scope',
    'content_type': 'Content type',
    'object_id': 'Object id',
    'name': 'Name',
    'responsible': 'Responsible',
    'target_date': 'Target date',
    'comments': 'Comments',
    'status': 'Status',
}

LABELS_BG = {
    'type': 'Тип',
    'scope': 'Обхват',
    'content_type': 'Тип съдържание',
    'object_id': 'ID на обект',
    'name': 'Име',
    'responsible': 'Отговорник',
    'target_date': 'Целева дата',
    'comments': 'Коментари',
    'status': 'Статус',
}

TYPE_CHOICES_BG = {
    ('Containment', 'Задържащо'),
    ('Correction', 'Корекция'),
    ('Corrective Action', 'Коригиращо действие'),
    ('Systematic Action', 'Систематично действие'),
    ('Improvement', 'Подобрение'),
    ('Task', 'Задача'),
}


class ActionFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].choices = TYPE_CHOICES_BG
            for field in self.fields:
                try:
                    self.fields[field].label = LABELS_BG[field]
                except KeyError:
                    pass


class ActionForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionFormRisk(ActionFormMixin, forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Risk.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='risk'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Corrective Action'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Risk') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)


class ActionFormOpportunity(ActionFormMixin, forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Opportunity.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='opportunity'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Improvement'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Opportunity') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)


class ActionFormNonconformity(forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Nonconformity.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='nonconformity'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].choices = [
            ('Containment', 'Containment'),
            ('Correction', 'Correction'),
            ('Corrective Action', 'Corrective Action'),
            ('Systematic Action', 'Systematic Action'),
        ]
        # self.fields['type'].widget = forms.Select(attrs={'class': 'select2'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Nonconformity') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].choices = [
                ('Containment', 'Задържане'),
                ('Correction', 'Корекция'),
                ('Corrective Action', 'Коригиращо действие'),
                ('Systematic Action', 'Систематично действие'),
            ]
            for field in self.fields:
                try:
                    self.fields[field].label = LABELS_BG[field]
                except KeyError:
                    pass


class ActionFormTask(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Task'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.fields['content_type'].initial = None
        self.fields['object_id'].initial = None

        self.change_labels_to_bg()


class ActionEditForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionEditFormRisk(ActionFormMixin, forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Risk.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='risk'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Corrective Action'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Risk') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)


class ActionEditFormOpportunity(ActionFormMixin, forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Opportunity.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='opportunity'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Improvement'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Opportunity') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)


class ActionEditFormNonconformity(forms.ModelForm):
    object_id = forms.ModelChoiceField(
        queryset=Nonconformity.objects.all(),
        to_field_name='id',
        label=_('Object ID'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid object ID')},
    )

    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model='nonconformity'),
        label=_('Content Type'),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'select2'}),
        error_messages={'invalid_choice': _('Select a valid content type')},
    )

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].choices = [
            ('Containment', 'Containment'),
            ('Correction', 'Correction'),
            ('Corrective Action', 'Corrective Action'),
            ('Systematic Action', 'Systematic Action'),
        ]
        # self.fields['type'].widget = forms.Select(attrs={'class': 'select2'})

        self.change_labels_to_bg()

        self.fields['content_type'].choices = [(content_type.id, 'Nonconformity') for content_type in self.fields['content_type'].queryset]

    def clean_object_id(self):
        object_id = self.cleaned_data['object_id'].id
        return int(object_id)

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].choices = [
                ('Containment', 'Задържане'),
                ('Correction', 'Корекция'),
                ('Corrective Action', 'Коригиращо действие'),
                ('Systematic Action', 'Систематично действие'),
            ]
            for field in self.fields:
                try:
                    self.fields[field].label = LABELS_BG[field]
                except KeyError:
                    pass


class ActionEditFormTask(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].initial = 'Task'
        self.fields['type'].widget = TextInput(attrs={'readonly': 'readonly'})

        self.fields['content_type'].initial = None
        self.fields['object_id'].initial = None

        self.change_labels_to_bg()


class ActionDeleteForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()
        # hide it
        self.fields['type'].widget = forms.HiddenInput()
        self.fields['scope'].widget = forms.HiddenInput()
        self.fields['content_type'].widget = forms.HiddenInput()
        self.fields['object_id'].widget = forms.HiddenInput()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class ActionViewForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class ActionTypeForm(forms.Form):
    action_type_dropdown = forms.ChoiceField(
        label='Action Type',
        choices=(('All', 'All'),),
    )

    # get a tuple suitable for 'choices' from a table
    @staticmethod
    def action_types():
        all_action_types = Action.objects.values_list('type', flat=True)
        all_action_types = list(set(all_action_types))
        action_types_tuples = [(item, item) for item in all_action_types]
        result = tuple(action_types_tuples)
        result = (('All', 'All'),) + result
        return result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['action_type_dropdown'].label = 'Вид на действието'

        self.fields['action_type_dropdown'].choices = self.action_types()
