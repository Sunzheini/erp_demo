from django.urls import path, include

from erp_demo.control_plan_mng.forms import ProcessControlPlanForm, ProcessControlPlanStepForm, \
    ProcessControlPlanEditForm, ProcessControlPlanStepEditForm, ProcessControlPlanDeleteForm, \
    ProcessControlPlanStepDeleteForm
from erp_demo.control_plan_mng.models import ProcessControlPlan, ProcessControlPlanStep
from erp_demo.control_plan_mng.views import ControlPlanMngViewsGeneral, \
    ControlPlanMngViewsControlPlan, ControlPlanMngViewsControlPlanStep


# Set-up
# ----------------------------------------------------------------------------------

template_list_control_plan = [
    None,
    None,
    None,
    'control_plan_mng/show_control_plan.html',
    'control_plan_mng/edit_control_plan.html',
    'control_plan_mng/delete_control_plan.html',
]

template_list_control_plan_step = [
    None,
    'control_plan_mng/control_plan_step_list.html',
    None,
    'control_plan_mng/show_control_plan_step.html',
    'control_plan_mng/edit_control_plan_step.html',
    'control_plan_mng/delete_control_plan_step.html',
]

redirect_url_control_plan = 'control plan mng index'
redirect_url_control_plan_step = 'control plan mng index'

form_list_control_plan = [
    # Create, View, Edit, Delete
    ProcessControlPlanForm, ProcessControlPlanForm, ProcessControlPlanEditForm, ProcessControlPlanDeleteForm,
]

form_list_control_plan_step = [
    # Create, View, Edit, Delete
    ProcessControlPlanStepForm, ProcessControlPlanStepForm, ProcessControlPlanStepEditForm, ProcessControlPlanStepDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', ControlPlanMngViewsGeneral().control_plan_mng_index, name='control plan mng index'),



    path('show-control-plan/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlan(
        template_list_control_plan, redirect_url_control_plan, form_list_control_plan, ProcessControlPlan, files_are_used
    ).show_view, name='show control plan'),

    path('edit-control-plan/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlan(
        template_list_control_plan, redirect_url_control_plan, form_list_control_plan, ProcessControlPlan, files_are_used
    ).edit_view, name='edit control plan'),

    path('delete-control-plan/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlan(
        template_list_control_plan, redirect_url_control_plan, form_list_control_plan, ProcessControlPlan, files_are_used
    ).delete_view, name='delete control plan'),



    path('show-control-plan-step/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlanStep(
        template_list_control_plan_step, redirect_url_control_plan_step, form_list_control_plan_step, ProcessControlPlanStep, files_are_used
    ).show_view, name='show control plan step'),

    path('edit-control-plan-step/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlanStep(
        template_list_control_plan_step, redirect_url_control_plan_step, form_list_control_plan_step, ProcessControlPlanStep, files_are_used
    ).edit_view, name='edit control plan step'),

    path('delete-control-plan-step/<int:pk>/<slug:slug>/', ControlPlanMngViewsControlPlanStep(
        template_list_control_plan_step, redirect_url_control_plan_step, form_list_control_plan_step, ProcessControlPlanStep, files_are_used
    ).delete_view, name='delete control plan step'),



    path('control-plan-step-list/', ControlPlanMngViewsControlPlanStep(
        template_list_control_plan_step, redirect_url_control_plan_step, form_list_control_plan_step, ProcessControlPlanStep, files_are_used
    ).list_view, name='control plan step list'),
]
