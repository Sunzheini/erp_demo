from django.shortcuts import render

from erp_demo.characteristics_mng.models import Characteristic
from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.defect_cat_mng.models import DefectCatalogueToCharacteristics


class DefectCatMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # updated
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)

        related_char_ids = DefectCatalogueToCharacteristics.objects.filter(
            defect_catalogue_id=current_object.pk).values_list('characteristic_id', flat=True)
        chars = Characteristic.objects.filter(id__in=related_char_ids)
        self.context['chars'] = chars

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)
