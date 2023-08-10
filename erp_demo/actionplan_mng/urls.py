from django.urls import path

from erp_demo.actionplan_mng.forms import ActionPlanForm, ActionPlanStepForm, \
    ActionPlanEditForm, ActionPlanDeleteForm, ActionPlanStepEditForm, \
    ActionPlanStepDeleteForm
from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep
from erp_demo.actionplan_mng.views import ActionPlanMngViewsGeneral, \
    ActionPlanMngViewsActionPlan, ActionPlanMngViewsActionPlanStep


# Set-up
# ----------------------------------------------------------------------------------

template_list_action_plan = [
    None,
    None,
    None,
    'actionplan_mng/show_actionplan.html',
    'actionplan_mng/edit_actionplan.html',
    'actionplan_mng/delete_actionplan.html',
]

template_list_action_plan_step = [
    None,
    None,
    None,
    'actionplan_mng/show_actionplan_step.html',
    'actionplan_mng/edit_actionplan_step.html',
    'actionplan_mng/delete_actionplan_step.html',
]

redirect_url_action_plan = 'action plan mng index'
redirect_url_action_plan_step = 'action plan mng index'

form_list_action_plan = [
    # Create, View, Edit, Delete
    ActionPlanForm, ActionPlanForm, ActionPlanEditForm, ActionPlanDeleteForm,
]

form_list_action_plan_step = [
    # Create, View, Edit, Delete
    ActionPlanStepForm, ActionPlanStepForm, ActionPlanStepEditForm, ActionPlanStepDeleteForm,
]

files_are_used = False

urlpatterns = [
    path('', ActionPlanMngViewsGeneral().action_plan_mng_index, name='action plan mng index'),



path('show-action-plan/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlan(
    template_list_action_plan, redirect_url_action_plan, form_list_action_plan, ActionPlan, files_are_used
).show_view, name='show action plan'),

path('edit-action-plan/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlan(
    template_list_action_plan, redirect_url_action_plan, form_list_action_plan, ActionPlan, files_are_used
).edit_view, name='edit action plan'),

path('delete-action-plan/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlan(
    template_list_action_plan, redirect_url_action_plan, form_list_action_plan, ActionPlan, files_are_used
).delete_view, name='delete action plan'),



path('show-action-plan-step/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlanStep(
    template_list_action_plan_step, redirect_url_action_plan_step, form_list_action_plan_step, ActionPlanStep, files_are_used
).show_view, name='show action plan step'),

path('edit-action-plan-step/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlanStep(
    template_list_action_plan_step, redirect_url_action_plan_step, form_list_action_plan_step, ActionPlanStep, files_are_used
).edit_view, name='edit action plan step'),

path('delete-action-plan-step/<int:pk>/<slug:slug>/', ActionPlanMngViewsActionPlanStep(
    template_list_action_plan_step, redirect_url_action_plan_step, form_list_action_plan_step, ActionPlanStep, files_are_used
).delete_view, name='delete action plan step'),
]
