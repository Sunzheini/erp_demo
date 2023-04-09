from django.urls import path, include

from erp_demo.organization_mng.views import OrgAppViews


urlpatterns = [
    path('', OrgAppViews().org_mng_index, name='org mng index'),
    path('org-list/', OrgAppViews().org_list, name='org list'),
    path('add-org/', OrgAppViews().add_org, name='add org'),
    path('show-org/<int:pk>/<slug:slug>/', OrgAppViews().show_org, name='show org'),
    path('edit-org/<int:pk>/<slug:slug>/', OrgAppViews().edit_org, name='edit org'),
    path('delete-org/<int:pk>/<slug:slug>/', OrgAppViews().delete_org, name='delete org'),
]
