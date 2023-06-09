from django.urls import path, include

from erp_demo.actions_mng.forms import ActionForm, ActionViewForm, ActionEditForm, ActionDeleteForm
from erp_demo.actions_mng.models import Action
from erp_demo.actions_mng.views import ActionsMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'actions_mng/actions_mng_index.html',
    'actions_mng/actions_list.html',
    'actions_mng/add_action.html',
    'actions_mng/show_action.html',
    'actions_mng/edit_action.html',
    'actions_mng/delete_action.html',
]

redirect_url = 'actions list'

form_list = [
    # Create, View, Edit, Delete
    ActionForm, ActionViewForm, ActionEditForm, ActionDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).index_view, name='actions mng index'),

    path('actions-list/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).list_view, name='actions list'),

    path('add-action/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).create_view, name='add action'),

    path('show-action/<int:pk>/<slug:slug>/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).show_view, name='show action'),

    path('edit-action/<int:pk>/<slug:slug>/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).edit_view, name='edit action'),

    path('delete-action/<int:pk>/<slug:slug>/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).delete_view, name='delete action'),


    path('get_related_objects/<int:content_type_id>/', ActionsMngViews(
        template_list, redirect_url, form_list, Action, files_are_used
    ).get_related_objects_view, name='get_related_objects'),
]
