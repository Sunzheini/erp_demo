from django.test import TestCase
from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep
from erp_demo.actionplan_mng.forms import ActionPlanDeleteForm, ActionPlanStepDeleteForm


class ActionPlanDeleteFormTests(TestCase):

    def test_save__when_instance_exists__expect_to_be_deleted(self):
        action_plan = ActionPlan.objects.create(name='Test Plan', description='Test Description')
        form = ActionPlanDeleteForm(instance=action_plan)

        form.save()

        self.assertFalse(ActionPlan.objects.filter(pk=action_plan.pk).exists())


class ActionPlanStepDeleteFormTests(TestCase):

    def test_save__when_instance_exists__expect_to_be_deleted(self):
        action_plan = ActionPlan.objects.create(name='Test Plan', description='Test Description')
        action_plan_step = ActionPlanStep.objects.create(number=1, scope='Test Scope', name='Test Name', parent_action_plan=action_plan)
        form = ActionPlanStepDeleteForm(instance=action_plan_step)

        form.save()

        self.assertFalse(ActionPlanStep.objects.filter(pk=action_plan_step.pk).exists())
