from django.shortcuts import render, redirect

from erp_demo.hr_mng.models import Employee
from erp_demo.main_app.forms import ManageDbHRForm, \
    ManageDbAllForm, DeleteDatabaseForm

from erp_demo.main_app.custom_logic import SupportFunctions


class MainAppViews:

    @staticmethod
    def index(request):
        context = {}
        return render(request, 'index.html', context)

    @staticmethod
    def contact_list(request):
        context = {}
        return render(request, 'core/contact_list.html', context)

    @staticmethod
    def manage_db(request):
        context = {}
        return render(request, 'core/manage_db.html', context)

    @staticmethod
    def manage_db_all(request):
        template = 'core/manage_db_all.html'
        message = None
        message2 = None

        if 'button_delete_db' in request.POST:
            form = DeleteDatabaseForm(request.POST)
            if form.is_valid():
                message = SupportFunctions.delete_database()
                form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()

        elif 'button_manage_db_all' in request.POST:
            form2 = ManageDbAllForm(request.POST, request.FILES)
            if form2.is_valid():
                message2 = SupportFunctions.recreate_database(request.FILES)
                form2 = ManageDbAllForm()
            form = DeleteDatabaseForm()

        else:
            form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()

        context = {
            'form': form,
            'form2': form2,
            'message': message,
            'message2': message2,
        }
        return render(request, template, context)
