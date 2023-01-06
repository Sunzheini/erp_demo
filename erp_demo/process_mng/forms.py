import os
from django import forms
from erp_demo.process_mng.models import Process, ProcessStep


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessStepForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = '__all__'
