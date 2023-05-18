from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.hr_mng.models import Employee
from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm, ProcessNumberForm
from erp_demo.process_mng.models import Process, ProcessStep


class ProcessMngViewsGeneral:
    @staticmethod
    @SupportFunctions.allow_groups()
    def process_mng_index(request):
        template = 'process_mng/process_mng_index.html'

        # choice = 'All'
        choice = None

        if 'button0' in request.POST:
            process_number_form = ProcessNumberForm(request.POST)
            if process_number_form.is_valid():
                choice = process_number_form.cleaned_data['process_number_dropdown']
            process_step_form = ProcessStepForm()
            process_form = ProcessForm()

        elif 'button1' in request.POST:
            process_form = ProcessForm(request.POST)
            if process_form.is_valid():
                process_form.save()
                process_form = ProcessForm()
            process_number_form = ProcessNumberForm()
            process_step_form = ProcessStepForm()

        elif 'button2' in request.POST:
            process_step_form = ProcessStepForm(request.POST)
            if process_step_form.is_valid():
                process_step_form.save()
                process_step_form = ProcessStepForm()
            process_number_form = ProcessNumberForm()
            process_form = ProcessForm()

        else:
            process_number_form = ProcessNumberForm()
            process_form = ProcessForm()
            process_step_form = ProcessStepForm()

        context = {
            'process_info': DataManipulation.sort_process_steps(
                Process,
                ProcessStep,
                choice,
            ),
            'choice_form': process_number_form,
            'process_form': process_form,
            'process_step_form': process_step_form,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_process_map(request):
        template = 'process_mng/process_map.html'

        context = {
            'all_objects': Process.objects.all(),
            'list_of_process_types': Process.objects.first().list_of_process_types,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_flowchart(request, pk):
        # template = 'process_mng/create_flowchart.html'
        template = 'process_mng/blank_flowchart.html'
        current_object = Process.objects.filter(pk=pk).get()
        context = {
            'current_object': current_object,
            'process_steps': DataManipulation.get_process_step_list(current_object, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_turtle(request, pk):
        # template = 'process_mng/create_turtle.html'
        template = 'process_mng/blank_turtle.html'
        current_object = Process.objects.filter(pk=pk).get()
        context = {
            'current_object': current_object,
            'process_steps': DataManipulation.get_process_step_list(current_object, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def process_owners(request):
        template = 'process_mng/process_owners.html'

        context = {
            'employees_w_owned_processes': DataManipulation.get_owned_processes_list(Employee, Process),
        }
        return render(request, template, context)


class ProcessMngViewsProcess(PrototypeViews):
    pass

class ProcessMngViewsProcessStep(PrototypeViews):
    pass
