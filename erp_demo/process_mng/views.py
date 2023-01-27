from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm, \
    ProcessStepEditForm, ProcessStepDeleteForm
from erp_demo.process_mng.models import Process, ProcessStep


class ProcessMngViews:
    @staticmethod
    def process_mng_index(request):
        template = 'process_mng/process_mng_index.html'

        if 'button1' in request.POST:
            process_form = ProcessForm(request.POST)
            if process_form.is_valid():
                process_form.save()
                process_form = ProcessForm()
            process_step_form = ProcessStepForm()

        elif 'button2' in request.POST:
            process_step_form = ProcessStepForm(request.POST)
            if process_step_form.is_valid():
                process_step_form.save()
                process_step_form = ProcessStepForm()
            process_form = ProcessForm()

        else:
            process_form = ProcessForm()
            process_step_form = ProcessStepForm()

        context = {
            'process_info': SupportFunctions.sort_process_steps(Process, ProcessStep),
            'process_form': process_form,
            'process_step_form': process_step_form,
        }
        return render(request, template, context)

    @staticmethod
    def edit_process_step(request, pk, slug):
        template = 'process_mng/edit_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessStepEditForm(instance=current_process_step)
        else:
            form = ProcessStepEditForm(request.POST, instance=current_process_step)
            if form.is_valid():
                form.save()
                return redirect('process mng index')
        context = {
            'form': form,
            'process_step': current_process_step,
        }
        return render(request, template, context)

    @staticmethod
    def delete_process_step(request, pk, slug):
        template = 'process_mng/delete_process_step.html'
        current_process_step = ProcessStep.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = ProcessStepDeleteForm(instance=current_process_step)
        else:
            form = ProcessStepDeleteForm(request.POST, instance=current_process_step)
            if form.is_valid():
                form.save()
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
