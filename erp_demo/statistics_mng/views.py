from django.shortcuts import render, redirect

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.custom_logic.extract_from_excel import extract_from_excel
from erp_demo.statistics_mng.forms import StatModel1UploadForm


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

    # specific vies for uploading the different physical forms

    @staticmethod
    def upload_model1_view(request):

    # make with inheritance and leave only this as unique when doing the next form
        current_form = StatModel1UploadForm
        model_name = 'StatModel1'
        template = 'statistics_mng/stat_model1/scan_stat_model1.html'
        rows_dict = {
            'name': 'D5',
            'operator': 'G5',
            'grinding': 'D7',
            'welding': 'D8',
            'blasting': 'D9',
            'painting': 'D10',
            'assembly': 'D11',
            'total_pieces': 'G7',
        }
    # -------------------------------------------------------------------------------

        app_name = 'statistics_mng'
        message = None

        if 'scan_record' in request.POST:
            form = current_form(request.POST, request.FILES)
            if form.is_valid():
                extract_from_excel(request.FILES, app_name, model_name, rows_dict)
                message = 'File uploaded successfully'
                form = current_form()
        else:
            form = current_form()

        context = {
            'form': form,
            'message': message,
        }

        return render(request, template, context)
