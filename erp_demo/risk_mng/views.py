from django.shortcuts import render

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.process_mng.models import Process


class RiskMngViews(PrototypeViews):
    def contingency_plan(self, request):
        try:
            all_objects = Process.objects.all()
        except Process.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Process} not found."})

        self.context = {
            'all_objects': all_objects,
        }

        try:
            return render(request, 'risk_mng/contingency_plan.html', self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
