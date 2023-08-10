from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews

from erp_demo.control_plan_mng.forms import ProcessControlPlanForm, ProcessControlPlanStepForm, ProcessControlPlanNameForm
from erp_demo.control_plan_mng.models import ProcessControlPlan, ProcessControlPlanStep, \
    ProcessControlPlanToProcessControlPlanStep


class ControlPlanMngViewsGeneral:
    @staticmethod
    @SupportFunctions.allow_groups()
    def control_plan_mng_index(request):
        template = 'control_plan_mng/control_plan_mng_index.html'
        context = {}

        all_objects = ProcessControlPlan.objects.all()

        if 'button0' in request.POST:
            control_plan_name_form = ProcessControlPlanNameForm(request.POST)
            if control_plan_name_form.is_valid():
                choice = control_plan_name_form.cleaned_data['process_control_plan']  # this line was changed

                if choice == 'all':
                    all_objects = ProcessControlPlan.objects.all()
                else:
                    # we are filtering by id here because we store the id in the choice field, not the name
                    all_objects = ProcessControlPlan.objects.filter(id=choice)

            control_plan_step_form = ProcessControlPlanStepForm()
            control_plan_form = ProcessControlPlanForm()

        elif 'button1' in request.POST:
            control_plan_form = ProcessControlPlanForm(request.POST)
            if control_plan_form.is_valid():
                control_plan_form.save()
                control_plan_form = ProcessControlPlanForm()
            else:
                context['has_form_errors'] = True
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_step_form = ProcessControlPlanStepForm()

        elif 'button2' in request.POST:
            control_plan_step_form = ProcessControlPlanStepForm(request.POST)
            if control_plan_step_form.is_valid():
                control_plan_step_form.save()
                control_plan_step_form = ProcessControlPlanStepForm()
            else:
                context['has_form_errors'] = True
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_form = ProcessControlPlanForm()

        else:
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_form = ProcessControlPlanForm()
            control_plan_step_form = ProcessControlPlanStepForm()

        # context = {
        #     'all_objects': all_objects,
        #     'choice_form': control_plan_name_form,
        #     'control_plan_form': control_plan_form,
        #     'control_plan_step_form': control_plan_step_form,
        # }

        context['all_objects'] = all_objects
        context['choice_form'] = control_plan_name_form
        context['control_plan_form'] = control_plan_form
        context['control_plan_step_form'] = control_plan_step_form

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})


class ControlPlanMngViewsControlPlan(PrototypeViews):
    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk, request)

        # updated
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        related_step_ids = ProcessControlPlanToProcessControlPlanStep.objects.filter(process_control_plan_id=current_object.pk).values_list('process_control_plan_step_id', flat=True)
        steps = ProcessControlPlanStep.objects.filter(id__in=related_step_ids)
        self.context['steps'] = steps

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)

        try:
            return render(request, self.show_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})


class ControlPlanMngViewsControlPlanStep(PrototypeViews):
    pass
