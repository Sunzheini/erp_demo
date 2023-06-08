from django.urls import path, include

from erp_demo.operations_mng.views import OperationsAppViews

urlpatterns = [
    path('', OperationsAppViews()
         .index, name='operations mng index'),
]
