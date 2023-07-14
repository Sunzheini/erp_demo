from django.core.exceptions import ValidationError
from django.test import TestCase

from erp_demo.actionplan_mng.models import ActionPlan


# Arrange, Act, Assert
class ActionPlanTests(TestCase):
    VALID_ACTION_PLAN_DATA = {
        'name': 'Test Action Plan',
        'description': 'Test Description',
    }

    def test_create__when_is_valid__expect_to_be_created(self):
        post = ActionPlan.objects.create(**self.VALID_ACTION_PLAN_DATA)

        # when testing models!!!
        post.full_clean()
        post.save()

        self.assertIsNotNone(post.pk)

    def test_create__when_name_has_1_more_than_valid_characters__expect_to_raise(self):
        invalid_data = {**self.VALID_ACTION_PLAN_DATA, 'name': 'n' * (ActionPlan.MAX_NAME_LENGTH + 1)}

        with self.assertRaises(ValidationError):
            post = ActionPlan(**invalid_data)

            # when testing models!!!
            post.full_clean()
            post.save()
