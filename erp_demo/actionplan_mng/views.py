from django.shortcuts import render

from collections import Counter

from erp_demo.actionplan_mng.models import ActionPlan
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.actionplan_mng.forms import ActionPlanForm, ActionPlanStepForm


class ActionPlanMngViewsGeneral:
    @staticmethod
    def action_plan_mng_index(request):
        template = 'actionplan_mng/actionplan_mng_index.html'

        # added
        action_plan_form = ActionPlanForm()
        action_plan_step_form = ActionPlanStepForm()

        if 'button1' in request.POST:
            # current code in try and also added except
            try:
                action_plan_form = ActionPlanForm(request.POST)
                if action_plan_form.is_valid():
                    action_plan_form.save()
                    action_plan_form = ActionPlanForm()
                action_plan_step_form = ActionPlanStepForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                action_plan_form.add_error(None, "An error occurred during form processing.")
                action_plan_step_form = ActionPlanStepForm()


        elif 'button2' in request.POST:
            # current code in try and also added except
            try:
                action_plan_step_form = ActionPlanStepForm(request.POST)
                if action_plan_step_form.is_valid():
                    action_plan_step_form.save()
                    action_plan_step_form = ActionPlanStepForm()
                action_plan_form = ActionPlanForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                action_plan_step_form.add_error(None, "An error occurred during form processing.")
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
    def show_view(self, request, pk, slug):
        self._empty_context()
        # added request
        current_object = self._main_object_single(pk, request)

        # updated for the graph
        # ---------------------------------------------------------------------------------------

        # Prepare pie chart data
        action_statuses = [action.action_id.status for step in current_object.get_all_steps for action in step.get_related_actions]

        action_status_distribution = dict(Counter(action_statuses))

        # Prepare chart data
        chart_data = {
            'labels': list(action_status_distribution.keys()),
            'datasets': [{
                'data': list(action_status_distribution.values()),
                'backgroundColor': ['rgb(245, 229, 81)', 'rgb(46, 139, 87)', 'rgb(128, 128, 128)'],  # adjust colors according to your status labels
            }]
        }

        self.context['chart_data'] = chart_data

        form = self.view_form(instance=current_object)

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)


class ActionPlanMngViewsActionPlanStep(PrototypeViews):
    pass

