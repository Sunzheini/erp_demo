from django.shortcuts import render, redirect

from erp_demo.customer_mng.models import Customer
from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.customer_mng.forms import CustomerForm, CustomerEditForm, CustomerDeleteForm, CustomerViewForm


class CustomerAppViews:
    @staticmethod
    def customer_mng_index(request):
        context = {}
        return render(request, 'customer_mng/customer_mng_index.html', context)

    @staticmethod
    def customer_list(request):
        template = 'customer_mng/customer_list.html'
        all_objects = Customer.objects.all()
        context = {
            'all_objects': all_objects,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def add_customer(request):
        template = 'customer_mng/add_customer.html'
        if request.method == 'GET':
            form = CustomerForm()
        else:
            form = CustomerForm(request.POST, request.FILES)
            if form.is_valid():
                output = form.save()  # get the created object
                SupportFunctions.log_info(f"Added a customer `{output.name}`")
                return redirect('customer list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def show_customer(request, pk, slug):
        template = 'customer_mng/show_customer.html'
        customer = Customer.objects.filter(pk=pk).get()
        form = CustomerViewForm(instance=customer)
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def edit_customer(request, pk, slug):
        template = 'customer_mng/edit_customer.html'
        customer = Customer.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = CustomerEditForm(instance=customer)
        else:
            form = CustomerEditForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited a customer `{output.name}`")
                return redirect('customer list')
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def delete_customer(request, pk, slug):
        template = 'customer_mng/delete_customer.html'
        customer = Customer.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = CustomerDeleteForm(instance=customer)
        else:
            form = CustomerDeleteForm(request.POST, instance=customer)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a customer `{output.name}`")
                return redirect('customer list')
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, template, context)
