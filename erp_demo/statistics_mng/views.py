from django.shortcuts import render

from erp_demo.custom_logic.custom_prototypes import PrototypeViews


class StatisticsMngViews(PrototypeViews):
    pass


class StatModel1Views(PrototypeViews):
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # updated
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        # Get the field values
        fields = ['grinding', 'welding', 'blasting', 'painting', 'assembly']
        values = {field: getattr(current_object, field) for field in fields}

        # Sort them in descending order
        sorted_values = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))

        # Prepare chart data
        chart_data = {
            'labels': list(sorted_values.keys()),
            'datasets': [{
                'data': list(sorted_values.values()),
                'fill': 'false',
                'backgroundColor': ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)'],
                'borderColor': ['rgb(255, 99, 132)', 'rgb(54, 162, 235)',
                                'rgb(255, 206, 86)', 'rgb(75, 192, 192)',
                                'rgb(153, 102, 255)'],
                'borderWidth': 1
            }]
        }

        self.context['chart_data'] = chart_data

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)
