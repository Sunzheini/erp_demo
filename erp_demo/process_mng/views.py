from django.shortcuts import render, redirect

from erp_demo.process_mng.forms import ProcessForm, ProcessStepForm
from erp_demo.process_mng.models import Process, ProcessStep, Document, ProcessStepToDocuments


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
        'processes': Process.objects.all(),
        'process_steps': ProcessStep.objects.all(),
        'process_form': process_form,
        'process_step_form': process_step_form,
    }
    return render(request, template, context)
