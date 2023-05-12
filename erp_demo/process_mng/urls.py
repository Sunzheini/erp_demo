from django.urls import path, include

from erp_demo.process_mng.forms import ProcessForm, ProcessEditForm, ProcessDeleteForm, \
    ProcessStepForm, ProcessStepEditForm, ProcessStepDeleteForm
from erp_demo.process_mng.models import Process, ProcessStep
from erp_demo.process_mng.views import ProcessMngViewsGeneral, ProcessMngViewsProcess, ProcessMngViewsProcessStep


# Set-up
# ----------------------------------------------------------------------------------

template_list_process = [
    None,
    None,
    None,
    'process_mng/show_process.html',
    'process_mng/edit_process.html',
    'process_mng/delete_process.html',
]

template_list_process_step = [
    None,
    None,
    None,
    'process_mng/show_process_step.html',
    'process_mng/edit_process_step.html',
    'process_mng/delete_process_step.html',
]

redirect_url_process = 'create process map'
redirect_url_process_step = 'process mng index'

form_list_process = [
    # Create, View, Edit, Delete
    ProcessForm, ProcessForm, ProcessEditForm, ProcessDeleteForm,
]

form_list_process_step = [
    # Create, View, Edit, Delete
    ProcessStepForm, ProcessStepForm, ProcessStepEditForm, ProcessStepDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', ProcessMngViewsGeneral().process_mng_index, name='process mng index'),

    path('process-map/', ProcessMngViewsGeneral().create_process_map, name='create process map'),

    path('create-flowchart/<int:pk>/', ProcessMngViewsGeneral().create_flowchart, name='create flowchart'),

    path('create-turtle/<int:pk>/', ProcessMngViewsGeneral().create_turtle, name='create turtle'),



    path('show-process/<int:pk>/<slug:slug>/', ProcessMngViewsProcess(
        template_list_process, redirect_url_process, form_list_process, Process, files_are_used
    ).show_view, name='show process'),

    path('edit-process/<int:pk>/<slug:slug>/', ProcessMngViewsProcess(
        template_list_process, redirect_url_process, form_list_process, Process, files_are_used
    ).edit_view, name='edit proces'),

    path('delete-process/<int:pk>/<slug:slug>/', ProcessMngViewsProcess(
        template_list_process, redirect_url_process, form_list_process, Process, files_are_used
    ).delete_view, name='delete process'),



    path('show-process-step/<int:pk>/<slug:slug>/', ProcessMngViewsProcessStep(
        template_list_process_step, redirect_url_process_step, form_list_process_step, ProcessStep, files_are_used
    ).show_view, name='show process step'),

    path('edit-process-step/<int:pk>/<slug:slug>/', ProcessMngViewsProcessStep(
        template_list_process_step, redirect_url_process_step, form_list_process_step, ProcessStep, files_are_used
    ).edit_view, name='edit process step'),

    path('delete-process-step/<int:pk>/<slug:slug>/', ProcessMngViewsProcessStep(
        template_list_process_step, redirect_url_process_step, form_list_process_step, ProcessStep, files_are_used
    ).delete_view, name='delete process step'),
]
