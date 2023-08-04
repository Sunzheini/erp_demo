from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.process_mng.models import Process


class OpportunityMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def opportunity_matrix(self, request):
        try:
            all_objects = Process.objects.all()
        except Process.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Process} not found."})

        context = {
            'all_objects': all_objects,
        }

        try:
            return render(request, 'opportunity_mng/opportunity_matrix.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
