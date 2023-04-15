from django.urls import path

from erp_demo.supplier_mng.views import TestListView

urlpatterns = [
    path('', TestListView.as_view(), name='supplier mng index'),
]