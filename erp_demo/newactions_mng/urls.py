from django.urls import path, include

from erp_demo.newactions_mng.forms import NewActionForm, NewActionViewForm, NewActionEditForm, NewActionDeleteForm
from erp_demo.newactions_mng.models import NewAction
from erp_demo.newactions_mng.views import NewActionsMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'newactions_mng/newactions_mng_index.html',
    'newactions_mng/newactions_list.html',
    'newactions_mng/add_newaction.html',
    'newactions_mng/show_newaction.html',
    'newactions_mng/edit_newaction.html',
    'newactions_mng/delete_newaction.html',
]

redirect_url = 'newactions list'

form_list = [
    # Create, View, Edit, Delete
    NewActionForm, NewActionViewForm, NewActionEditForm, NewActionDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).index_view, name='newactions mng index'),

    path('actions-list/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).list_view, name='newactions list'),

    path('add-action/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).create_view, name='add newaction'),

    path('show-action/<int:pk>/<slug:slug>/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).show_view, name='show newaction'),

    path('edit-action/<int:pk>/<slug:slug>/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).edit_view, name='edit newaction'),

    path('delete-action/<int:pk>/<slug:slug>/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).delete_view, name='delete newaction'),


    path('actions-matrix/', NewActionsMngViews(
        template_list, redirect_url, form_list, NewAction, files_are_used
    ).actions_matrix, name='newactions matrix'),
]
