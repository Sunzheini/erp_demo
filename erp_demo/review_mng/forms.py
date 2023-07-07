from django import forms
from django.utils import translation

from erp_demo.review_mng.models import ManagementReview


LABELS_EN = {
    'name': 'Management review name',
    'date': 'Date',
    'status_from_previous_reviews': 'Status from previous reviews',
    'external_and_internal_changes': 'External and internal changes',
    'customer_feedback': 'Customer feedback',
    'kpis': 'KPIs',
    'kpis_comments': 'KPIs comments',
    'other_kpis': 'Other KPIs',
    'nonconformities': 'Nonconformities',
    'nonconformities_comments': 'Nonconformities comments',
    'audit_results': 'Audit results',
    'suppliers': 'Suppliers',
    'suppliers_comments': 'Suppliers comments',
    'resources': 'Resources',
    'resources_comments': 'Resources comments',
    'risks': 'Risks',
    'risks_comments': 'Risks comments',
    'opportunities': 'Opportunities',
    'opportunities_comments': 'Opportunities comments',
    'costs_of_poor_quality': 'Costs of poor quality',
    'manufacturing_feasibility': 'Manufacturing feasibility',
    'other_topics': 'Other topics',
}


LABELS_BG = {
    'name': 'Име на прегледа от ръководството',
    'date': 'Дата',
    'status_from_previous_reviews': 'Статус от предишни прегледи',
    'external_and_internal_changes': 'Външни и вътрешни промени',
    'customer_feedback': 'Отзиви от клиенти',
    'kpis': 'Показатели',
    'kpis_comments': 'Коментари към показателите',
    'other_kpis': 'Други показатели',
    'nonconformities': 'Несъответствия',
    'nonconformities_comments': 'Коментари към несъответствията',
    'audit_results': 'Резултати от oдити',
    'suppliers': 'Доставчици',
    'suppliers_comments': 'Коментари към доставчиците',
    'resources': 'Ресурси',
    'resources_comments': 'Коментари към ресурсите',
    'risks': 'Рискове',
    'risks_comments': 'Коментари към рисковете',
    'opportunities': 'Възможности',
    'opportunities_comments': 'Коментари към възможностите',
    'costs_of_poor_quality': 'Разходи за лошо качество',
    'manufacturing_feasibility': 'Производствена изпълнимост',
    'other_topics': 'Други теми',
}


class ManagementReviewFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for field_name, label in self.fields.items():
                self.fields[field_name].label = LABELS_BG[field_name]


class ManagementReviewForm(ManagementReviewFormMixin, forms.ModelForm):
    class Meta:
        model = ManagementReview
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ManagementReviewEditForm(ManagementReviewFormMixin, forms.ModelForm):
    class Meta:
        model = ManagementReview
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ManagementReviewDeleteForm(ManagementReviewFormMixin, forms.ModelForm):
    class Meta:
        model = ManagementReview
        exclude = ['slug']

        labels = LABELS_EN

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


class ManagementReviewViewForm(ManagementReviewFormMixin, forms.ModelForm):
    class Meta:
        model = ManagementReview
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
