from django.shortcuts import render

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.supplier_mng.models import Supplier


class SupplierMngViews(PrototypeViews):
    @staticmethod
    def supplier_scores(request):
        suppliers = Supplier.objects.all().order_by('-score')  # descending order by score

        supplier_names = [supplier.name for supplier in suppliers]
        supplier_scores = [supplier.score for supplier in suppliers]

        chart_data = {
            'labels': supplier_names,
            'datasets': [{
                'label': 'Supplier Score',
                'data': supplier_scores,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',  # change color to fit your style
                'borderColor': 'rgba(75, 192, 192, 1)',  # change color to fit your style
                'borderWidth': 1
            }]
        }

        context = {
            'all_objects': suppliers,
            'chart_data': chart_data,
        }

        try:
            return render(request, 'supplier_mng/supplier_scores.html', context)
        except Exception as e:
            print(f"Exception: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
