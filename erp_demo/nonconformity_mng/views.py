import getpass

from django.shortcuts import redirect

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.custom_logic.extract_to_excel import ExtractToExcel
from erp_demo.nonconformity_mng.models import Nonconformity


class NonconformityMngViews(PrototypeViews):
    def write_to_excel(self, request, pk, slug):
        my_object = Nonconformity.objects.filter(pk=pk).get()

        # Get username of the currently logged in OS user
        username = getpass.getuser()

        path = f'C:\\Users\\{username}\\Desktop\\8D_' + my_object.name[:20] + '.xlsx'
        extractor = ExtractToExcel(path, my_object)

        try:
            extractor.run()
        except Exception as e:
            print(f"Exception: {e}")

        return redirect(self.redirect_url)
