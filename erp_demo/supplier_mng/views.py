from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from erp_demo.dox_mng.models import Document


class TestListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'


#  delete
class SupplierListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'


class SupplierDetailView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'


class SupplierCreateView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'


def supplier_mng_index(request):
    return render(request, 'supplier_mng/supplier_mng_index.html')
