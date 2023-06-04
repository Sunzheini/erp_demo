from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.process_mng.models import Process


class OpportunityMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def opportunity_matrix(self, request):
        context = {
            'all_objects': Process.objects.all(),
        }
        return render(request, 'opportunity_mng/opportunity_matrix.html', context)
