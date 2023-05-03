from django.urls import path

from erp_demo.supplier_mng.views import TestListView, another_view

urlpatterns = [
    # path('', TestListView.as_view(), name='supplier mng index'),
    path('', another_view, name='supplier mng index'),
]
