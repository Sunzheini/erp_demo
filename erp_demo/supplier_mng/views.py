import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.core.cache import cache

from erp_demo.dox_mng.models import Document
from erp_demo.main_app.custom_logic import SupportFunctions


class TestListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'supplier_mng/supplier_mng_index.html'


# 0.018s
@cache_page(1 * 60) # 1 minute
def another_view(request):
    value = random.randint(1, 1024)

    return render(request, 'supplier_mng/supplier_mng_index.html', {
        'document_list': Document.objects.all(),
        'value': value,
    })
