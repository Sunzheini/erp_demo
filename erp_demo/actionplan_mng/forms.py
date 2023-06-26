from django import forms
from django.utils import translation

from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep


ACTION_PLAN_LABELS_EN = {
    'name': 'Name',
    'description': 'Description',
    'owner': 'Owner',
}

ACTION_PLAN_LABELS_BG = {
    'name': 'Име',
    'description': 'Описание',
    'owner': 'Собственик',
}

ACTION_PLAN_STEP_LABELS_EN = {
    'number': 'Number',
    'scope': 'Scope',
    'name': 'Name',
    'parent_action_plan': 'Parent Action Plan',
    'actions': 'Actions',
}

ACTION_PLAN_STEP_LABELS_BG = {
    'number': 'Номер',
    'scope': 'Обхват',
    'name': 'Име',
    'parent_action_plan': 'Към План за Действие',
    'actions': 'Действия',
}


class ActionPlanMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = ACTION_PLAN_LABELS_BG['name']
            self.fields['description'].label = ACTION_PLAN_LABELS_BG['description']
            self.fields['owner'].label = ACTION_PLAN_LABELS_BG['owner']


class ActionPlanStepMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['number'].label = ACTION_PLAN_STEP_LABELS_BG['number']
            self.fields['scope'].label = ACTION_PLAN_STEP_LABELS_BG['scope']
            self.fields['name'].label = ACTION_PLAN_STEP_LABELS_BG['name']
            self.fields['parent_action_plan'].label = ACTION_PLAN_STEP_LABELS_BG['parent_action_plan']
            self.fields['actions'].label = ACTION_PLAN_STEP_LABELS_BG['actions']


class ActionPlanForm(ActionPlanMixin, forms.ModelForm):
    class Meta:
        model = ActionPlan
        fields = '__all__'

        labels = ACTION_PLAN_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionPlanStepForm(ActionPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ActionPlanStep
        fields = '__all__'

        labels = ACTION_PLAN_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionPlanEditForm(ActionPlanMixin, forms.ModelForm):
    class Meta:
        model = ActionPlan
        fields = '__all__'

        labels = ACTION_PLAN_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionPlanStepEditForm(ActionPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ActionPlanStep
        fields = '__all__'

        labels = ACTION_PLAN_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionPlanDeleteForm(ActionPlanMixin, forms.ModelForm):
    class Meta:
        model = ActionPlan
        fields = '__all__'

        labels = ACTION_PLAN_LABELS_EN

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


class ActionPlanStepDeleteForm(ActionPlanStepMixin, forms.ModelForm):
    class Meta:
        model = ActionPlanStep
        fields = '__all__'

        labels = ACTION_PLAN_STEP_LABELS_EN

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














