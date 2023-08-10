from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews

from django.core.serializers.json import DjangoJSONEncoder
import json


class MaintenanceMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def list_view(self, request):
        self._empty_context()

        # updated
        # ---------------------------------------------------------------------------------------
        all_objects = self._main_object_queryset(request)

        green_limit = 30
        yellow_limit = -1

        machines_count_1 = 0
        machines_count_2 = 0
        machines_count_3 = 0

        for machine in all_objects:
            distance = machine.distance_to_maintenance_deadline
            if distance is not None:
                if distance > green_limit:
                    machines_count_1 += 1
                elif yellow_limit < distance <= green_limit:
                    machines_count_2 += 1
                elif distance <= yellow_limit:
                    machines_count_3 += 1

        chart_data = {
            'labels': ['> 30', '1 - 30', '< 1'],
            'datasets': [{
                # 'label': 'Number of Machines',
                'data': [machines_count_1, machines_count_2, machines_count_3],
                'backgroundColor': ['#2e8b57', '#f5e751', '#bd1515'],
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }]
        }
        max_value = max(machines_count_1, machines_count_2, machines_count_3)
        self.context['max_value'] = max_value

        self.context['chart_data'] = json.dumps(chart_data, cls=DjangoJSONEncoder)
        self.context['all_objects'] = all_objects
        self.context['green_limit'] = green_limit
        self.context['yellow_limit'] = yellow_limit

        # ---------------------------------------------------------------------------------------

        try:
            return render(request, self.list_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk, request)

        # updated
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        green_limit = 30
        yellow_limit = -1
        self.context['green_limit'] = green_limit
        self.context['yellow_limit'] = yellow_limit
        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)

        try:
            return render(request, self.show_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})
