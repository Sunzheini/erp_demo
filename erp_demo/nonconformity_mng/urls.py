from django.urls import path, include

from erp_demo.nonconformity_mng.views import NonconformityMngViews

urlpatterns = [
    path('', NonconformityMngViews()
         .index, name='nonconformity mng index'),
]
