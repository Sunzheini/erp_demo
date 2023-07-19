from django.test import TestCase
from django.urls import reverse

from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep


class IndexViewTests(TestCase):
    def test_index__when_get_request__expect_no_new_instances_and_correct_template(self):
        action_plans_before = ActionPlan.objects.count()
        action_plan_steps_before = ActionPlanStep.objects.count()

        response = self.client.get(
            reverse('action plan mng index')
        )

        action_plans_after = ActionPlan.objects.count()
        action_plan_steps_after = ActionPlanStep.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(action_plans_after, action_plans_before)
        self.assertEqual(action_plan_steps_after, action_plan_steps_before)
        self.assertTemplateUsed(response, 'actionplan_mng/actionplan_mng_index.html')

    def test_index__when_button1_posted__expect_post_data_in_context(self):
        post_data = {
            'button1': '',
            'name': 'value123',
            'description': 'value245'
        }

        action_plans_before = ActionPlan.objects.count()

        response = self.client.post(
            reverse('action plan mng index'),
            data=post_data
        )

        action_plans_after = ActionPlan.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'actionplan_mng/actionplan_mng_index.html')
        self.assertEqual(action_plans_after, action_plans_before + 1)

    def test_index__when_button2_posted__expect_post_data_in_context(self):
        post_data = {
            'button2': '',
            'number': 1,
            'scope': 'value3',
            'name': 'value4',
        }

        response = self.client.post(
            reverse('action plan mng index'),
            data=post_data
        )

        cleaned_data = response.context['action_plan_step_form'].cleaned_data

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'actionplan_mng/actionplan_mng_index.html')
        self.assertEqual(cleaned_data['number'], post_data['number'])
        self.assertEqual(cleaned_data['scope'], post_data['scope'])
        self.assertEqual(cleaned_data['name'], post_data['name'])
