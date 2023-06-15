from django.shortcuts import render

from erp_demo.actionplan_mng.models import ActionPlan
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.actionplan_mng.forms import ActionPlanForm, ActionPlanStepForm


class ActionPlanMngViewsGeneral:
    @staticmethod
    def action_plan_mng_index(request):
        template = 'actionplan_mng/actionplan_mng_index.html'

        if 'button1' in request.POST:
            action_plan_form = ActionPlanForm(request.POST)
            if action_plan_form.is_valid():
                action_plan_form.save()
                action_plan_form = ActionPlanForm()
            action_plan_step_form = ActionPlanStepForm()

        elif 'button2' in request.POST:
            action_plan_step_form = ActionPlanStepForm(request.POST)
            if action_plan_step_form.is_valid():
                action_plan_step_form.save()
                action_plan_step_form = ActionPlanStepForm()
            action_plan_form = ActionPlanForm()

        else:
            action_plan_form = ActionPlanForm()
            action_plan_step_form = ActionPlanStepForm()

        context = {
            'all_objects': ActionPlan.objects.all(),
            'action_plan_form': action_plan_form,
            'action_plan_step_form': action_plan_step_form,
        }
        return render(request, template, context)


class ActionPlanMngViewsActionPlan(PrototypeViews):
    pass


class ActionPlanMngViewsActionPlanStep(PrototypeViews):
    pass

