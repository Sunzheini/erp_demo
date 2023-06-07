from django.urls import path, include

from erp_demo.resource_mng.forms import ResourceForm, ResourceViewForm, ResourceEditForm, ResourceDeleteForm
from erp_demo.resource_mng.models import Resource
from erp_demo.resource_mng.views import ResourceMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'resource_mng/resource_mng_index.html',
    'resource_mng/resource_list.html',
    'resource_mng/add_resource.html',
    'resource_mng/show_resource.html',
    'resource_mng/edit_resource.html',
    'resource_mng/delete_resource.html',
]

redirect_url = 'resource list'

form_list = [
    # Create, View, Edit, Delete
    ResourceForm, ResourceViewForm, ResourceEditForm, ResourceDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).index_view, name='resource mng index'),

    path('resource-list/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).list_view, name='resource list'),

    path('add-resource/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).create_view, name='add resource'),

    path('show-resource/<int:pk>/<slug:slug>/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).show_view, name='show resource'),

    path('edit-resource/<int:pk>/<slug:slug>/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).edit_view, name='edit resource'),

    path('delete-resource/<int:pk>/<slug:slug>/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).delete_view, name='delete resource'),

    path('assign-resources/', ResourceMngViews(
        template_list, redirect_url, form_list, Resource, files_are_used
    ).assign_resources, name='assign resources'),
]
