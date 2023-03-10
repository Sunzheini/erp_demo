from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm, \
    ProcessStepEditForm, ProcessStepDeleteForm, \
    ProcessEditForm, ProcessDeleteForm, ProcessNumberForm
from erp_demo.process_mng.models import Process, ProcessStep


class ProcessMngViews:
    # @staticmethod
    # def process_mng_index(request):
    #     template = 'process_mng/process_mng_index.html'
    #
    #     if 'button1' in request.POST:
    #         process_form = ProcessForm(request.POST)
    #         if process_form.is_valid():
    #             process_form.save()
    #             process_form = ProcessForm()
    #         process_step_form = ProcessStepForm()
    #
    #     elif 'button2' in request.POST:
    #         process_step_form = ProcessStepForm(request.POST)
    #         if process_step_form.is_valid():
    #             process_step_form.save()
    #             process_step_form = ProcessStepForm()
    #         process_form = ProcessForm()
    #
    #     else:
    #         process_form = ProcessForm()
    #         process_step_form = ProcessStepForm()
    #
    #     context = {
    #         'process_info': SupportFunctions.sort_process_steps(Process, ProcessStep),
    #         'process_form': process_form,
    #         'process_step_form': process_step_form,
    #     }
    #     return render(request, template, context)

    @staticmethod
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
            'process_info': SupportFunctions.sort_process_steps(Process, ProcessStep, choice),
            'choice_form': process_number_form,
            'process_form': process_form,
            'process_step_form': process_step_form,
        }
        return render(request, template, context)

    @staticmethod
    def show_process_step(request, pk, slug):
        template = 'process_mng/show_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        context = {
            'process_step': current_process_step,
        }
        return render(request, template, context)

    @staticmethod
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
    def create_flowchart(request, pk):
        template = 'process_mng/create_flowchart.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
            'process_steps': SupportFunctions.get_process_step_list(current_process, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    def create_turtle(request, pk):
        template = 'process_mng/create_turtle.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
            'process_steps': SupportFunctions.get_process_step_list(current_process, ProcessStep)
        }
        return render(request, template, context)

    @staticmethod
    def create_process_map(request):
        template = 'process_mng/process_map.html'
        context = {
            'processes': Process.objects.all(),
        }
        return render(request, template, context)

    @staticmethod
    def show_process(request, pk, slug):
        template = 'process_mng/show_process.html'
        current_process = Process.objects.filter(pk=pk).get()
        context = {
            'process': current_process,
        }
        return render(request, template, context)

    @staticmethod
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
