from django import forms
from django.utils import translation

from erp_demo.control_plan_mng.models import ProcessControlPlan, ProcessControlPlanStep


PROCESS_CONTROL_PLAN_LABELS_EN = {
    'name': 'Name',
    'type': 'Type',
    'number': 'Number',
    'revision': 'Revision',
    'creation_date': 'Creation date',
    'update_date': 'Update date',
    'product': 'Product',
    'owner': 'Owner',
    'team': 'Team',
    'steps': 'Steps',
}

PROCESS_CONTROL_PLAN_LABELS_BG = {
    'name': 'Име',
    'type': 'Тип',
    'number': 'Номер',
    'revision': 'Ревизия',
    'creation_date': 'Дата създаване',
    'update_date': 'Дата обновяване',
    'product': 'Продукт',
    'owner': 'Собственик',
    'team': 'Екип',
    'steps': 'Стъпки',
}

PROCESS_CONTROL_PLAN_STEP_LABELS_EN = {
    'name': 'Name',
    'machines': 'Machines',
    'characteristics': 'Characteristics',
    'measuring_equipment': 'Measuring equipment',
    'sample_size': 'Sample size',
    'frequency': 'Frequency',
    'documents': 'Documents',
    'reaction_plan': 'Reaction plan',
}

PROCESS_CONTROL_PLAN_STEP_LABELS_BG = {
    'name': 'Име',
    'machines': 'Машини',
    'characteristics': 'Характеристики',
    'measuring_equipment': 'Измервателни уреди',
    'sample_size': 'Размер проба',
    'frequency': 'Честота',
    'documents': 'Документи',
    'reaction_plan': 'План реакция',
}

PROCESS_CONTROL_PLAN_CHOICES_BG=(
    ('Prototype', 'Прототип'),
    ('Pre-launch', 'Предпроизводство'),
    ('Production', 'Производство'),
)

PROCESS_CONTROL_PLAN_NAME_LABELS_EN = {
    'name': 'Name',
}

PROCESS_CONTROL_PLAN_NAME_LABELS_BG = {
    'name': 'Име',
}


class ProcessControlPlanMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].label = PROCESS_CONTROL_PLAN_LABELS_BG['type']
            self.fields['type'].choices = PROCESS_CONTROL_PLAN_CHOICES_BG

            self.fields['name'].label = PROCESS_CONTROL_PLAN_LABELS_BG['name']
            self.fields['number'].label = PROCESS_CONTROL_PLAN_LABELS_BG['number']
            self.fields['revision'].label = PROCESS_CONTROL_PLAN_LABELS_BG['revision']
            self.fields['creation_date'].label = PROCESS_CONTROL_PLAN_LABELS_BG['creation_date']
            self.fields['update_date'].label = PROCESS_CONTROL_PLAN_LABELS_BG['update_date']
            self.fields['product'].label = PROCESS_CONTROL_PLAN_LABELS_BG['product']
            self.fields['owner'].label = PROCESS_CONTROL_PLAN_LABELS_BG['owner']
            self.fields['team'].label = PROCESS_CONTROL_PLAN_LABELS_BG['team']
            self.fields['steps'].label = PROCESS_CONTROL_PLAN_LABELS_BG['steps']


class ProcessControlPlanStepMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['name']
            self.fields['machines'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['machines']
            self.fields['characteristics'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['characteristics']
            self.fields['measuring_equipment'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['measuring_equipment']
            self.fields['sample_size'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['sample_size']
            self.fields['frequency'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['frequency']
            self.fields['documents'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['documents']
            self.fields['reaction_plan'].label = PROCESS_CONTROL_PLAN_STEP_LABELS_BG['reaction_plan']


class ProcessControlPlanForm(ProcessControlPlanMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlan
        exclude = ['creation_date', 'update_date']

        labels = PROCESS_CONTROL_PLAN_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessControlPlanStepForm(ProcessControlPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlanStep
        fields = '__all__'

        labels = PROCESS_CONTROL_PLAN_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessControlPlanEditForm(ProcessControlPlanMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlan
        exclude = ['creation_date', 'update_date']

        labels = PROCESS_CONTROL_PLAN_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessControlPlanStepEditForm(ProcessControlPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlanStep
        fields = '__all__'

        labels = PROCESS_CONTROL_PLAN_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessControlPlanDeleteForm(ProcessControlPlanMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlan
        exclude = ['creation_date', 'update_date']

        labels = PROCESS_CONTROL_PLAN_LABELS_EN

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


class ProcessControlPlanStepDeleteForm(ProcessControlPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ProcessControlPlanStep
        fields = '__all__'

        labels = PROCESS_CONTROL_PLAN_STEP_LABELS_EN

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


# class ProcessControlPlanNameForm(forms.Form):
#     def change_labels_to_bg(self):
#         language_code = translation.get_language()
#         if language_code == 'bg':
#             self.fields['name'].label = PROCESS_CONTROL_PLAN_NAME_LABELS_BG['name']
#
#     name = forms.ModelChoiceField(
#         queryset=ProcessControlPlan.objects.all(),
#         label=PROCESS_CONTROL_PLAN_NAME_LABELS_EN['name'],
#         to_field_name="name",
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.change_labels_to_bg()


class ProcessControlPlanNameForm(forms.Form):
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['process_control_plan'].label = PROCESS_CONTROL_PLAN_NAME_LABELS_BG['name']

    process_control_plan = forms.ChoiceField(
        label=PROCESS_CONTROL_PLAN_NAME_LABELS_EN['name'],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['process_control_plan'].choices = [('all', 'All')] + [(pcp.id, pcp.name) for pcp in ProcessControlPlan.objects.all()]
        self.change_labels_to_bg()


