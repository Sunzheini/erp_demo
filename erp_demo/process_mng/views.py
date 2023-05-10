from django.shortcuts import render, redirect
from django.views import View

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm, \
    ProcessStepEditForm, ProcessStepDeleteForm, \
    ProcessEditForm, ProcessDeleteForm, ProcessNumberForm
from erp_demo.process_mng.models import Process, ProcessStep

# -------------------------------------------------------------
# trying with a class based view

# class ProcessMngIndexView(SupportFunctions, View):
#     template_name = 'process_mng/process_mng_index.html'
#
#     @SupportFunctions.allow_groups()
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         process_number_form = ProcessNumberForm()
#         process_form = ProcessForm()
#         process_step_form = ProcessStepForm()
#         context = self.get_context(process_number_form, process_form, process_step_form)
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         process_number_form = ProcessNumberForm(request.POST)
#         process_form = ProcessForm(request.POST)
#         process_step_form = ProcessStepForm(request.POST)
#
#         if 'button0' in request.POST and process_number_form.is_valid():
#             choice = process_number_form.cleaned_data['process_number_dropdown']
#             process_step_form = ProcessStepForm()
#             process_form = ProcessForm()
#
#         elif 'button1' in request.POST and process_form.is_valid():
#             process_form.save()
#             process_form = ProcessForm()
#             process_number_form = ProcessNumberForm()
#             process_step_form = ProcessStepForm()
#
#         elif 'button2' in request.POST and process_step_form.is_valid():
#             process_step_form.save()
#             process_step_form = ProcessStepForm()
#             process_number_form = ProcessNumberForm()
#             process_form = ProcessForm()
#
#         else:
#             process_number_form = ProcessNumberForm()
#             process_form = ProcessForm()
#             process_step_form = ProcessStepForm()
#
#         context = self.get_context(process_number_form, process_form, process_step_form, choice)
#         return render(request, self.template_name, context)
#
#     @staticmethod
#     def get_context(process_number_form, process_form, process_step_form, choice=None):
#         return {
#             'process_info': SupportFunctions.sort_process_steps(Process, ProcessStep, choice),
#             'choice_form': process_number_form,
#             'process_form': process_form,
#             'process_step_form': process_step_form,
#         }


# -------------------------------------------------------------

class ProcessMngViews:
    @staticmethod
    @SupportFunctions.allow_groups()
    # @SupportFunctions.measure_time
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
            'process_info': SupportFunctions.sort_process_steps(
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
    def show_process_step(request, pk, slug):
        template = 'process_mng/show_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        context = {
            'process_step': current_process_step,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def edit_process_step(request, pk, slug):
        template = 'process_mng/edit_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessStepEditForm(instance=current_process_step)
        else:
            form = ProcessStepEditForm(request.POST, instance=current_process_step)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited a process step `{output.name}`")
                return redirect('process mng index')
        context = {
            'form': form,
            'process_step': current_process_step,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def delete_process_step(request, pk, slug):
        template = 'process_mng/delete_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessStepDeleteForm(instance=current_process_step)
        else:
            form = ProcessStepDeleteForm(request.POST, instance=current_process_step)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a process step `{output.name}`")
                return redirect('process mng index')
        context = {
            'form': form,
            'process_step': current_process_step,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_flowchart(request, pk):
        # template = 'process_mng/create_flowchart.html'
        template = 'process_mng/blank_flowchart.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
            'process_steps': SupportFunctions.get_process_step_list(current_process, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_turtle(request, pk):
        # template = 'process_mng/create_turtle.html'
        template = 'process_mng/blank_turtle.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
            'process_steps': SupportFunctions.get_process_step_list(current_process, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def create_process_map(request):
        template = 'process_mng/process_map.html'
        context = {
            'processes': Process.objects.all(),
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    def show_process(request, pk, slug):
        template = 'process_mng/show_process.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def edit_process(request, pk, slug):
        template = 'process_mng/edit_process.html'
        current_process = Process.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessEditForm(instance=current_process)
        else:
            form = ProcessEditForm(request.POST, instance=current_process)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited a process `{output.name}`")
                return redirect('create process map')
        context = {
            'form': form,
            'process': current_process,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def delete_process(request, pk, slug):
        template = 'process_mng/delete_process.html'
        current_process = Process.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessDeleteForm(instance=current_process)
        else:
            form = ProcessDeleteForm(request.POST, instance=current_process)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a process `{output.name}`")
                return redirect('create process map')
        context = {
            'form': form,
            'process': current_process,
        }
        return render(request, template, context)
