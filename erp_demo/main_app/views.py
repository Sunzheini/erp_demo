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
    def manage_db_hr(request):
        template = 'core/manage_db_hr.html'
        message = None
        if request.method == 'GET':
            form = ManageDbHRForm()
        else:
            form = ManageDbHRForm(request.POST, request.FILES)
            if form.is_valid():
                message = SupportFunctions.add_to_database(request.FILES)
                # return redirect('manage db')
                context = {
                    'form': form,
                    'message': message,
                }
                return render(request, template, context)
        context = {
            'form': form,
            'message': message,
        }
        return render(request, template, context)

    # @staticmethod
    # def manage_db_all(request):
    #     template = 'core/manage_db_all.html'
    #     message = None
    #     if 'button_delete_db' in request.POST:
    #         form = DeleteDatabaseForm(request.POST)
    #         if form.is_valid():
    #             message = SupportFunctions.delete_database()
    #             context = {
    #                 'form': form,
    #                 'message': message,
    #             }
    #             return render(request, template, context)
    #     else:
    #         form = DeleteDatabaseForm()
    #     context = {
    #         'form': form,
    #         'message': message,
    #     }
    #     return render(request, template, context)

    @staticmethod
    def manage_db_all(request):
        template = 'core/manage_db_all.html'
        message = None
        if 'button_delete_db' in request.POST:
            form = DeleteDatabaseForm(request.POST)
            form2 = ManageDbAllForm()
            if form.is_valid():
                message = SupportFunctions.delete_database()
                context = {
                    'form': form,
                    'form2': form2,
                    'message': message,
                }
                return render(request, template, context)
        else:
            form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()
        context = {
            'form': form,
            'form2': form2,
            'message': message,
        }
        return render(request, template, context)