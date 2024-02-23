from django import forms
from django.utils import translation
from erp_demo.analytics.models import Analysis


ANALYSIS_LABELS_EN = {
    'name': 'Name',
    'code': 'Code',
    'measurement_unit': 'Measurement unit',

    'material1': 'Material 1',
    'material2': 'Material 2',
    'material3': 'Material 3',
    'material4': 'Material 4',
    'material5': 'Material 5',
    'position1': 'Position 1',
    'position2': 'Position 2',
    'position3': 'Position 3',
    'position4': 'Position 4',
    'position5': 'Position 5',
    'machine1': 'Machine 1',
    'machine2': 'Machine 2',
    'machine3': 'Machine 3',
    'machine4': 'Machine 4',
    'machine5': 'Machine 5',

    'material1_measurement_unit': 'Material 1 measurement unit',
    'material2_measurement_unit': 'Material 2 measurement unit',
    'material3_measurement_unit': 'Material 3 measurement unit',
    'material4_measurement_unit': 'Material 4 measurement unit',
    'material5_measurement_unit': 'Material 5 measurement unit',
    'position1_measurement_unit': 'Position 1 measurement unit',
    'position2_measurement_unit': 'Position 2 measurement unit',
    'position3_measurement_unit': 'Position 3 measurement unit',
    'position4_measurement_unit': 'Position 4 measurement unit',
    'position5_measurement_unit': 'Position 5 measurement unit',
    'machine1_measurement_unit': 'Machine 1 measurement unit',
    'machine2_measurement_unit': 'Machine 2 measurement unit',
    'machine3_measurement_unit': 'Machine 3 measurement unit',
    'machine4_measurement_unit': 'Machine 4 measurement unit',
    'machine5_measurement_unit': 'Machine 5 measurement unit',

    'material1_cost_rate': 'Material 1 cost rate',
    'material2_cost_rate': 'Material 2 cost rate',
    'material3_cost_rate': 'Material 3 cost rate',
    'material4_cost_rate': 'Material 4 cost rate',
    'material5_cost_rate': 'Material 5 cost rate',
    'position1_cost_rate': 'Position 1 cost rate',
    'position2_cost_rate': 'Position 2 cost rate',
    'position3_cost_rate': 'Position 3 cost rate',
    'position4_cost_rate': 'Position 4 cost rate',
    'position5_cost_rate': 'Position 5 cost rate',
    'machine1_cost_rate': 'Machine 1 cost rate',
    'machine2_cost_rate': 'Machine 2 cost rate',
    'machine3_cost_rate': 'Machine 3 cost rate',
    'machine4_cost_rate': 'Machine 4 cost rate',
    'machine5_cost_rate': 'Machine 5 cost rate',

    'material1_price': 'Material 1 price',
    'material2_price': 'Material 2 price',
    'material3_price': 'Material 3 price',
    'material4_price': 'Material 4 price',
    'material5_price': 'Material 5 price',
    'position1_price': 'Position 1 price',
    'position2_price': 'Position 2 price',
    'position3_price': 'Position 3 price',
    'position4_price': 'Position 4 price',
    'position5_price': 'Position 5 price',
    'machine1_price': 'Machine 1 price',
    'machine2_price': 'Machine 2 price',
    'machine3_price': 'Machine 3 price',
    'machine4_price': 'Machine 4 price',
    'machine5_price': 'Machine 5 price',

    'material1_total': 'Material 1 total',
    'material2_total': 'Material 2 total',
    'material3_total': 'Material 3 total',
    'material4_total': 'Material 4 total',
    'material5_total': 'Material 5 total',
    'position1_total': 'Position 1 total',
    'position2_total': 'Position 2 total',
    'position3_total': 'Position 3 total',
    'position4_total': 'Position 4 total',
    'position5_total': 'Position 5 total',
    'machine1_total': 'Machine 1 total',
    'machine2_total': 'Machine 2 total',
    'machine3_total': 'Machine 3 total',
    'machine4_total': 'Machine 4 total',
    'machine5_total': 'Machine 5 total',

    'additional_expense_materials_cost_rate': 'Additional expense materials cost rate',
    'additional_expense_positions_cost_rate': 'Additional expense positions cost rate',
    'additional_expense_machines_cost_rate': 'Additional expense machines cost rate',
    'additional_expense_materials_total': 'Additional expense materials total',
    'additional_expense_positions_total': 'Additional expense positions total',
    'additional_expense_machines_total': 'Additional expense machines total',

    'total_direct_costs': 'Total direct costs',
    'total_additional_costs': 'Total additional costs',

    'total_costs': 'Total costs',
    'profit': 'Profit',
    'final_price': 'Final price',
}

ANALYSIS_LABELS_BG = {
    'name': 'Име',
    'code': 'Код',
    'measurement_unit': 'Мерна единица',

    'material1': 'Материал 1',
    'material2': 'Материал 2',
    'material3': 'Материал 3',
    'material4': 'Материал 4',
    'material5': 'Материал 5',
    'position1': 'Позиция 1',
    'position2': 'Позиция 2',
    'position3': 'Позиция 3',
    'position4': 'Позиция 4',
    'position5': 'Позиция 5',
    'machine1': 'Машина 1',
    'machine2': 'Машина 2',
    'machine3': 'Машина 3',
    'machine4': 'Машина 4',
    'machine5': 'Машина 5',

    'material1_measurement_unit': 'Мерна единица на материал 1',
    'material2_measurement_unit': 'Мерна единица на материал 2',
    'material3_measurement_unit': 'Мерна единица на материал 3',
    'material4_measurement_unit': 'Мерна единица на материал 4',
    'material5_measurement_unit': 'Мерна единица на материал 5',
    'position1_measurement_unit': 'Мерна единица на позиция 1',
    'position2_measurement_unit': 'Мерна единица на позиция 2',
    'position3_measurement_unit': 'Мерна единица на позиция 3',
    'position4_measurement_unit': 'Мерна единица на позиция 4',
    'position5_measurement_unit': 'Мерна единица на позиция 5',
    'machine1_measurement_unit': 'Мерна единица на машина 1',
    'machine2_measurement_unit': 'Мерна единица на машина 2',
    'machine3_measurement_unit': 'Мерна единица на машина 3',
    'machine4_measurement_unit': 'Мерна единица на машина 4',
    'machine5_measurement_unit': 'Мерна единица на машина 5',

    'material1_cost_rate': 'Разходна норма на материал 1',
    'material2_cost_rate': 'Разходна норма на материал 2',
    'material3_cost_rate': 'Разходна норма на материал 3',
    'material4_cost_rate': 'Разходна норма на материал 4',
    'material5_cost_rate': 'Разходна норма на материал 5',
    'position1_cost_rate': 'Разходна норма на позиция 1',
    'position2_cost_rate': 'Разходна норма на позиция 2',
    'position3_cost_rate': 'Разходна норма на позиция 3',
    'position4_cost_rate': 'Разходна норма на позиция 4',
    'position5_cost_rate': 'Разходна норма на позиция 5',
    'machine1_cost_rate': 'Разходна норма на машина 1',
    'machine2_cost_rate': 'Разходна норма на машина 2',
    'machine3_cost_rate': 'Разходна норма на машина 3',
    'machine4_cost_rate': 'Разходна норма на машина 4',
    'machine5_cost_rate': 'Разходна норма на машина 5',

    'material1_price': 'Цена на материал 1',
    'material2_price': 'Цена на материал 2',
    'material3_price': 'Цена на материал 3',
    'material4_price': 'Цена на материал 4',
    'material5_price': 'Цена на материал 5',
    'position1_price': 'Цена на позиция 1',
    'position2_price': 'Цена на позиция 2',
    'position3_price': 'Цена на позиция 3',
    'position4_price': 'Цена на позиция 4',
    'position5_price': 'Цена на позиция 5',
    'machine1_price': 'Цена на машина 1',
    'machine2_price': 'Цена на машина 2',
    'machine3_price': 'Цена на машина 3',
    'machine4_price': 'Цена на машина 4',
    'machine5_price': 'Цена на машина 5',

    'material1_total': 'Общо за материал 1',
    'material2_total': 'Общо за материал 2',
    'material3_total': 'Общо за материал 3',
    'material4_total': 'Общо за материал 4',
    'material5_total': 'Общо за материал 5',
    'position1_total': 'Общо за позиция 1',
    'position2_total': 'Общо за позиция 2',
    'position3_total': 'Общо за позиция 3',
    'position4_total': 'Общо за позиция 4',
    'position5_total': 'Общо за позиция 5',
    'machine1_total': 'Общо за машина 1',
    'machine2_total': 'Общо за машина 2',
    'machine3_total': 'Общо за машина 3',
    'machine4_total': 'Общо за машина 4',
    'machine5_total': 'Общо за машина 5',

    'additional_expense_materials_cost_rate': 'Допълнителни разходи за материали разходна норма',
    'additional_expense_positions_cost_rate': 'Допълнителни разходи за позиции разходна норма',
    'additional_expense_machines_cost_rate': 'Допълнителни разходи за машини разходна норма',
    'additional_expense_materials_total': 'Допълнителни разходи за материали общо',
    'additional_expense_positions_total': 'Допълнителни разходи за позиции общо',
    'additional_expense_machines_total': 'Допълнителни разходи за машини общо',

    'total_direct_costs': 'Всичко преки разходи',
    'total_additional_costs': 'Всичко допълнителни разходи',

    'total_costs': 'Общо разходи',
    'profit': 'Печалба',
    'final_price': 'Крайна цена',
}


class AnalysisModelAndExcludeMixin:
    model = Analysis
    exclude = ['slug']

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for name, field in self.fields.items():
                field.label = ANALYSIS_LABELS_BG[name]
        else:
            for name, field in self.fields.items():
                field.label = ANALYSIS_LABELS_EN[name]


class AnalysisForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class AnalysisEditForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class AnalysisDeleteForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class AnalysisViewForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
