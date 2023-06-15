from django.shortcuts import render

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.supplier_mng.models import Supplier


class SupplierMngViews(PrototypeViews):
    def supplier_scores(self, request):
        context = {
            'all_objects': Supplier.objects.all(),
        }
        return render(request, 'supplier_mng/supplier_scores.html', context)
