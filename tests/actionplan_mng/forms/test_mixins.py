from django.test import TestCase
from django.utils import translation

from erp_demo.actionplan_mng.forms import ActionPlanForm, ActionPlanStepForm, ActionPlanMixin, ActionPlanStepMixin, \
    ACTION_PLAN_LABELS_BG, ACTION_PLAN_STEP_LABELS_BG


class ActionPlanMixinTests(TestCase):
    def setUp(self):
        self.original_language = translation.get_language()
        self.form = ActionPlanForm()

    def test_change_labels_to_bg__when_language_is_bg__expect_to_change_labels(self):
        translation.activate('bg')

        self.form.change_labels_to_bg()

        self.assertEqual(self.form.fields['name'].label, ACTION_PLAN_LABELS_BG['name'])
        self.assertEqual(self.form.fields['description'].label, ACTION_PLAN_LABELS_BG['description'])
        self.assertEqual(self.form.fields['owner'].label, ACTION_PLAN_LABELS_BG['owner'])

    def tearDown(self):
        translation.activate(self.original_language)


class ActionPlanStepMixinTests(TestCase):
    def setUp(self):
        self.original_language = translation.get_language()
        self.form = ActionPlanStepForm()

    def test_change_labels_to_bg__when_language_is_bg__expect_to_change_labels(self):
        translation.activate('bg')

        self.form.change_labels_to_bg()

        self.assertEqual(self.form.fields['number'].label, ACTION_PLAN_STEP_LABELS_BG['number'])
        self.assertEqual(self.form.fields['scope'].label, ACTION_PLAN_STEP_LABELS_BG['scope'])
        self.assertEqual(self.form.fields['name'].label, ACTION_PLAN_STEP_LABELS_BG['name'])
        self.assertEqual(self.form.fields['parent_action_plan'].label, ACTION_PLAN_STEP_LABELS_BG['parent_action_plan'])
        self.assertEqual(self.form.fields['actions'].label, ACTION_PLAN_STEP_LABELS_BG['actions'])

    def tearDown(self):
        translation.activate(self.original_language)
