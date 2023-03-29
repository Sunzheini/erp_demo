from django.urls import path, include

from erp_demo.organization_mng.views import OrgAppViews


urlpatterns = [
    path('', OrgAppViews().index, name='org mng index'),
    path('org-list/', OrgAppViews().org_list, name='org list'),
]
