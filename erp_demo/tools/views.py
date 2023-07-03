import getpass

from django.shortcuts import render, redirect

from erp_demo.control_plan_mng.models import ProcessControlPlan
from erp_demo.process_mng.models import Process
from erp_demo.tools.forms import AuditProcessNumberForm, AuditProcessControlPlanNameForm
from erp_demo.custom_logic.extract_to_excel import ExtractToExcel


class ToolsMngViews:
    @staticmethod
    def generate_system_checklist(request):
        template = 'tools/generate_system_checklist.html'

        if 'button0' in request.POST:
            process_number_form = AuditProcessNumberForm(request.POST)
            if process_number_form.is_valid():

                choice = process_number_form.cleaned_data['process_number_dropdown']
                my_object = Process.objects.filter(number=choice).get()

                list_of_process_steps = my_object.processstep_set.all()
                additional_fields = ['number', 'name']

                # Get username of the currently logged in OS user
                username = getpass.getuser()

                path = f'C:\\Users\\{username}\\Desktop\\Audit_Checklist_' + my_object.number + '.xlsx'
                extractor = ExtractToExcel(
                    path,
                    my_object,
                    additional_object_list=list_of_process_steps,
                    fields=additional_fields,
                )

                try:
                    extractor.run()
                except Exception as e:
                    print(f"Exception: {e}")

                return redirect('generate system checklist')


        else:
            process_number_form = AuditProcessNumberForm()

        context = {
            'choice_form': process_number_form,
        }
        return render(request, template, context)

    @staticmethod
    def generate_process_checklist(request):
        template = 'tools/generate_process_checklist.html'

        if 'button0' in request.POST:
            control_plan_form = AuditProcessControlPlanNameForm(request.POST)
            if control_plan_form.is_valid():

                choice = control_plan_form.cleaned_data['process_control_plan']
                print(choice)
                my_object = ProcessControlPlan.objects.filter(id=choice).get()

                list_of_process_steps = my_object.steps.all()
                additional_fields = ['name']

                # Get username of the currently logged in OS user
                username = getpass.getuser()

                path = f'C:\\Users\\{username}\\Desktop\\Audit_Checklist_' + my_object.number + '.xlsx'
                extractor = ExtractToExcel(
                    path,
                    my_object,
                    additional_object_list=list_of_process_steps,
                    fields=additional_fields,
                )

                try:
                    extractor.run()
                except Exception as e:
                    print(f"Exception: {e}")

                return redirect('generate system checklist')


        else:
            control_plan_form = AuditProcessControlPlanNameForm()

        context = {
            'choice_form': control_plan_form,
        }
        return render(request, template, context)
