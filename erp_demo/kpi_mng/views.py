from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.process_mng.models import Process


class KpiMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # updated for the graph
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        # Prepare chart data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        actual_values = [getattr(current_object, f"actual_{str(month).zfill(2)}_23") or 0 for month in range(1, 13)]
        target_value = float(current_object.target)  # ensure that target is converted to float
        chart_data = {
            'labels': months,
            'datasets': [{
                # 'label': current_object.name,
                'data': actual_values,
                'fill': 'false',  # changed this
                'borderColor': 'rgb(75, 192, 192)',
                # 'borderColor': 'rgb(0, 0, 139)',
                'tension': 0.1
            },
            {
                'data': [target_value]*12,  # repeat target value for each month
                'fill': 'false',
                'borderColor': 'rgb(255, 0, 0)',  # change the color to distinguish from actual values
                'tension': 0.1
            }
            ]
        }

        self.context['chart_data'] = chart_data

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)

    @SupportFunctions.login_check
    def kpi_matrix(self, request):
        self.context = {
            'all_objects': Process.objects.all(),
        }

        return render(request, 'kpi_mng/kpi_matrix.html', self.context)

