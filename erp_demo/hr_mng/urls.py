from django.urls import path, include

from erp_demo.hr_mng.views import HrMngViews


urlpatterns = [
    path('', HrMngViews().index_view, name='hr mng index'),
]
