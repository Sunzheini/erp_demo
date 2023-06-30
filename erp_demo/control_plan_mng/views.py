from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.hr_mng.models import Employee

from erp_demo.control_plan_mng.forms import ProcessControlPlanForm, ProcessControlPlanStepForm, \
    ProcessControlPlanEditForm, ProcessControlPlanStepEditForm, ProcessControlPlanDeleteForm, \
    ProcessControlPlanStepDeleteForm, ProcessControlPlanNameForm
from erp_demo.control_plan_mng.models import ProcessControlPlan, ProcessControlPlanStep, \
    ProcessControlPlanToProcessControlPlanStep


class ControlPlanMngViewsGeneral:
    @staticmethod
    @SupportFunctions.allow_groups()
    def control_plan_mng_index(request):
        template = 'control_plan_mng/control_plan_mng_index.html'

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
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_step_form = ProcessControlPlanStepForm()

        elif 'button2' in request.POST:
            control_plan_step_form = ProcessControlPlanStepForm(request.POST)
            if control_plan_step_form.is_valid():
                control_plan_step_form.save()
                control_plan_step_form = ProcessControlPlanStepForm()
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_form = ProcessControlPlanForm()

        else:
            control_plan_name_form = ProcessControlPlanNameForm()
            control_plan_form = ProcessControlPlanForm()
            control_plan_step_form = ProcessControlPlanStepForm()

        context = {
            'all_objects': all_objects,
            'choice_form': control_plan_name_form,
            'control_plan_form': control_plan_form,
            'control_plan_step_form': control_plan_step_form,
        }
        return render(request, template, context)


class ControlPlanMngViewsControlPlan(PrototypeViews):
    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # updated
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        related_step_ids = ProcessControlPlanToProcessControlPlanStep.objects.filter(process_control_plan_id=current_object.pk).values_list('process_control_plan_step_id', flat=True)
        steps = ProcessControlPlanStep.objects.filter(id__in=related_step_ids)
        self.context['steps'] = steps

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)


class ControlPlanMngViewsControlPlanStep(PrototypeViews):
    pass
