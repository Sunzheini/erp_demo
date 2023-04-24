from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from erp_demo.dox_mng.models import Document


class TestListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'



