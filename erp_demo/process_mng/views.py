import threading

from django.shortcuts import render

from erp_demo.custom_logic.parallels import CustomThread
from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.hr_mng.models import Employee
from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm, ProcessNumberForm
from erp_demo.process_mng.models import Process, ProcessStep
from erp_demo.resource_mng.models import ResourcesAssignedToProcess


class ProcessMngViewsGeneral:
    @staticmethod
    @SupportFunctions.allow_groups()
    def process_mng_index(request):
        template = 'process_mng/process_mng_index.html'

        # choice = 'All'
        choice = None
        process_number_form = ProcessNumberForm()
        process_form = ProcessForm()
        process_step_form = ProcessStepForm()

        if 'button0' in request.POST:
            try:
                process_number_form = ProcessNumberForm(request.POST)
                if process_number_form.is_valid():
                    choice = process_number_form.cleaned_data['process_number_dropdown']
                process_step_form = ProcessStepForm()
                process_form = ProcessForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                process_number_form.add_error(None, "An error occurred during form processing.")
                process_step_form = ProcessStepForm()
                process_form = ProcessForm()

        elif 'button1' in request.POST:
            try:
                process_form = ProcessForm(request.POST)
                if process_form.is_valid():
                    process_form.save()
                    process_form = ProcessForm()
                process_number_form = ProcessNumberForm()
                process_step_form = ProcessStepForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                process_form.add_error(None, "An error occurred during form processing.")
                process_number_form = ProcessNumberForm()
                process_step_form = ProcessStepForm()

        elif 'button2' in request.POST:
            try:
                process_step_form = ProcessStepForm(request.POST)
                if process_step_form.is_valid():
                    process_step_form.save()
                    process_step_form = ProcessStepForm()
                process_number_form = ProcessNumberForm()
                process_form = ProcessForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                process_step_form.add_error(None, "An error occurred during form processing.")
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

        try:
            return render(request, template, context)
        except Exception as e:
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_process_map(request):
        template = 'process_mng/process_map.html'

        try:
            all_objects = Process.objects.all()
        except Process.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Process} not found."})

        context = {
            'all_objects': all_objects,
            'list_of_process_types': Process.objects.first().list_of_process_types,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_flowchart(request, pk):
        # template = 'process_mng/create_flowchart.html'
        template = 'process_mng/blank_flowchart.html'

        try:
            current_object = Process.objects.filter(pk=pk).get()
        except Process.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Process} not found."})

        context = {
            'current_object': current_object,
            'process_steps': DataManipulation.get_process_step_list(current_object, ProcessStep)
        }

        try:
            return render(request, template, context)
        except Exception as e:
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    # @staticmethod
    # @SupportFunctions.allow_groups()
    # def create_turtle(request, pk):
    #     # template = 'process_mng/create_turtle.html'
    #     template = 'process_mng/blank_turtle.html'
    #     current_object = Process.objects.filter(pk=pk).get()
    #     context = {
    #         'current_object': current_object,
    #         'process_steps': DataManipulation.get_process_step_list(current_object, ProcessStep),
    #     }
    #     return render(request, template, context)

    # @staticmethod
    # @SupportFunctions.allow_groups()
    # def create_turtle(request, pk):
    #     # template = 'process_mng/create_turtle.html'
    #     template = 'process_mng/blank_turtle.html'
    #
    #     try:
    #         current_object = Process.objects.filter(pk=pk).get()
    #     except Process.DoesNotExist:
    #         return render(request, 'error.html', {'error_message': f"{Process} not found."})
    #
    #     process_steps = DataManipulation.get_process_step_list(current_object, ProcessStep)
    #     from_interactions = DataManipulation.get_from_interactions_list(current_object)
    #     to_interactions = DataManipulation.get_to_interactions_list(current_object)
    #
    #     try:
    #         resources = ResourcesAssignedToProcess.objects.filter(process=current_object)
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")
    #         return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
    #
    #     context = {
    #         'current_object': current_object,
    #         'process_steps': process_steps,
    #         'from_interactions': from_interactions,
    #         'to_interactions': to_interactions,
    #         'resources': resources,
    #     }
    #
    #     try:
    #         return render(request, template, context)
    #     except Exception as e:
    #         return render(request, 'error.html',
    #                       {'error_message': f'An unexpected error occurred: {e}.'})

    # @staticmethod
    # @SupportFunctions.allow_groups()
    # def create_turtle(request, pk):
    #     # template = 'process_mng/create_turtle.html'
    #     template = 'process_mng/blank_turtle.html'
    #
    #     try:
    #         current_object = Process.objects.filter(pk=pk).get()
    #     except Process.DoesNotExist:
    #         return render(request, 'error.html', {'error_message': f"{Process} not found."})
    #
    #     process_steps = DataManipulation.get_process_step_list(current_object, ProcessStep)
    #     from_interactions = DataManipulation.get_from_interactions_list(current_object)
    #     to_interactions = DataManipulation.get_to_interactions_list(current_object)
    #
    #     try:
    #         resources = ResourcesAssignedToProcess.objects.filter(process=current_object)
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")
    #         return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
    #
    #     context = {
    #         'current_object': current_object,
    #         'process_steps': process_steps,
    #         'from_interactions': from_interactions,
    #         'to_interactions': to_interactions,
    #         'resources': resources,
    #     }
    #
    #     try:
    #         return render(request, template, context)
    #     except Exception as e:
    #         return render(request, 'error.html',
    #                       {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_turtle(request, pk):
        # template = 'process_mng/create_turtle.html'
        template = 'process_mng/blank_turtle.html'

        try:
            current_object = Process.objects.filter(pk=pk).get()
        except Process.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Process} not found."})

        def get_the_process_steps():
            return DataManipulation.get_process_step_list(current_object, ProcessStep)

        def get_the_from_interactions():
            return DataManipulation.get_from_interactions_list(current_object)

        def get_the_to_interactions():
            return DataManipulation.get_to_interactions_list(current_object)

        thread1 = CustomThread(target=get_the_process_steps)
        thread2 = CustomThread(target=get_the_from_interactions)
        thread3 = CustomThread(target=get_the_to_interactions)

        thread1.start()
        thread2.start()
        thread3.start()

        process_steps = thread1.join()
        from_interactions = thread2.join()
        to_interactions = thread3.join()

        try:
            resources = ResourcesAssignedToProcess.objects.filter(process=current_object)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

        context = {
            'current_object': current_object,
            'process_steps': process_steps,
            'from_interactions': from_interactions,
            'to_interactions': to_interactions,
            'resources': resources,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def process_owners(request):
        template = 'process_mng/process_owners.html'

        context = {
            'employees_w_owned_processes': DataManipulation.get_owned_processes_list(Employee, Process),
        }

        try:
            return render(request, template, context)
        except Exception as e:
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})


class ProcessMngViewsProcess(PrototypeViews):
    pass

class ProcessMngViewsProcessStep(PrototypeViews):
    pass
