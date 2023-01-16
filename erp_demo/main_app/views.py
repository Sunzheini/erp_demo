from django.shortcuts import render, redirect
from erp_demo.main_app.forms import ManageDbForm

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
        template = 'core/manage_db.html'
        message = None

        if request.method == 'GET':
            form = ManageDbForm()
        else:
            form = ManageDbForm(request.POST, request.FILES)
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
