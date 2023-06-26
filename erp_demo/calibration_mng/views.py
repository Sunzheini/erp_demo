from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews

from django.core.serializers.json import DjangoJSONEncoder
import json


class CalibrationMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def list_view(self, request):
        self._empty_context()

        # updated
        # ---------------------------------------------------------------------------------------
        all_objects = self._main_object_queryset()

        green_limit = 30
        yellow_limit = -1

        equipment_count_1 = 0
        equipment_count_2 = 0
        equipment_count_3 = 0

        for equipment in all_objects:
            distance = equipment.distance_to_calibration_deadline
            if distance is not None:
                if distance > green_limit:
                    equipment_count_1 += 1
                elif yellow_limit < distance <= green_limit:
                    equipment_count_2 += 1
                elif distance <= yellow_limit:
                    equipment_count_3 += 1

        chart_data = {
            'labels': ['> 30', '1 - 30', '< 1'],
            'datasets': [{
                # 'label': 'Number of Equipment',
                'data': [equipment_count_1, equipment_count_2, equipment_count_3],
                # 'backgroundColor': 'rgba(75, 192, 192, 0.2)',  # change color to fit your style
                'backgroundColor': ['#2e8b57', '#f5e751', '#bd1515'],
                'borderColor': 'rgba(75, 192, 192, 1)',  # change color to fit your style
                'borderWidth': 1
            }]
        }

        max_value = max(equipment_count_1, equipment_count_2, equipment_count_3)
        self.context['max_value'] = max_value

        self.context['chart_data'] = json.dumps(chart_data, cls=DjangoJSONEncoder)
        self.context['all_objects'] = all_objects
        self.context['green_limit'] = green_limit
        self.context['yellow_limit'] = yellow_limit

        # ---------------------------------------------------------------------------------------

        return render(request, self.list_template, self.context)

    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

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
        return render(request, self.show_template, self.context)
