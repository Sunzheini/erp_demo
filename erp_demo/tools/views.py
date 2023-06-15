import getpass

from django.shortcuts import render, redirect

from erp_demo.process_mng.models import Process
from erp_demo.tools.forms import AuditProcessNumberForm
from erp_demo.custom_logic.extract_to_excel import ExtractToExcel


class ToolsMngViews:
    @staticmethod
    def generate_system_checklist(request):
        template = 'tools/generate_system_checklist.html'

        choice = None

        if 'button0' in request.POST:
            process_number_form = AuditProcessNumberForm(request.POST)
            if process_number_form.is_valid():

                choice = process_number_form.cleaned_data['process_number_dropdown']
                my_object = Process.objects.filter(number=choice).get()

                # Get username of the currently logged in OS user
                username = getpass.getuser()

                path = f'C:\\Users\\{username}\\Desktop\\Audit_Checklist_' + my_object.number + '.xlsx'
                extractor = ExtractToExcel(path, my_object)

                try:
                    extractor.run()
                except Exception as e:
                    print(f"Exception: {e}")

                return redirect('generate system checklist')


        else:
            process_number_form = AuditProcessNumberForm()

        context = {
            'choice_form': process_number_form,
        }
        return render(request, template, context)
