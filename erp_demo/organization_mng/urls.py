from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from erp_demo.organization_mng.views import OrgAppViews
from erp_demo.organization_mng.forms import OrgForm, OrgEditForm, OrgDeleteForm, OrgViewForm
from erp_demo.organization_mng.models import Organization

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'organization_mng/org_mng_index.html',
    'organization_mng/org_list.html',
    'organization_mng/add_org.html',
    'organization_mng/show_org.html',
    'organization_mng/edit_org.html',
    'organization_mng/delete_org.html',
]

redirect_url = 'org list'

form_list = [
    # Create, View, Edit, Delete
    OrgForm, OrgViewForm, OrgEditForm, OrgDeleteForm,
]

files_are_used = True

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).index_view, name='org mng index'),

    path('org-list/', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).list_view, name='org list'),

    path('add-org/', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).create_view, name='add org'),

    path('show-org/<int:pk>/<slug:slug>/', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).show_view, name='show org'),

    path('edit-org/<int:pk>/<slug:slug>/', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).edit_view, name='edit org'),

    path('delete-org/<int:pk>/<slug:slug>/', OrgAppViews(
        template_list, redirect_url, form_list, Organization, files_are_used
    ).delete_view, name='delete org'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
