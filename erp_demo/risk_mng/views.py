from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.process_mng.models import Process


class RiskMngViews(PrototypeViews):
    def contingency_plan(self, request):
        self.context = {
            'all_objects': Process.objects.all(),
        }
        return render(request, 'risk_mng/contingency_plan.html', self.context)
