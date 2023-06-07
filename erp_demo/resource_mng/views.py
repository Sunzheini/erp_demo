from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.resource_mng.forms import ResourceAssignToEmployeeForm, ChangeForm, ResourceAssignToProcessForm
from erp_demo.resource_mng.models import ResourcesAssignedToEmployees, ResourcesAssignedToProcess


class ResourceMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def assign_resources(self, request):
        if 'buttonx' in request.POST:
            form = ResourceAssignToEmployeeForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['quantity'] > form.cleaned_data['resource'].available_quantity:
                    form.add_error('quantity', 'Not enough resources available')
                else:
                    form.save()
                    form = ResourceAssignToEmployeeForm()
            change_form = ChangeForm()
            form2 = ResourceAssignToProcessForm()

        elif 'buttony' in request.POST:
            form2 = ResourceAssignToProcessForm(request.POST)
            if form2.is_valid():
                if form2.cleaned_data['quantity'] > form2.cleaned_data['resource'].available_quantity:
                    form2.add_error('quantity', 'Not enough resources available')
                else:
                    form2.save()
                    form2 = ResourceAssignToProcessForm()
            form = ResourceAssignToEmployeeForm()
            change_form = ChangeForm()

        elif 'buttonz1' in request.POST:
            change_form = ChangeForm(request.POST)
            if change_form.is_valid():
                current_object_id = request.POST.get('current_object_id')
                current_object = ResourcesAssignedToEmployees.objects.get(id=current_object_id)
                new_quantity = change_form.cleaned_data['new_quantity']

                if new_quantity == 0:
                    current_object.delete()
                elif new_quantity > current_object.resource.available_quantity + current_object.quantity:
                    change_form.add_error('new_quantity', 'You cannot assign more resources than available')
                else:
                    current_object.quantity = new_quantity
                    current_object.save()
                change_form = ChangeForm()
            form = ResourceAssignToEmployeeForm()
            form2 = ResourceAssignToProcessForm()

        elif 'buttonz2' in request.POST:
            change_form = ChangeForm(request.POST)
            if change_form.is_valid():
                current_object_id = request.POST.get('current_object_id')
                current_object = ResourcesAssignedToProcess.objects.get(id=current_object_id)
                new_quantity = change_form.cleaned_data['new_quantity']

                if new_quantity == 0:
                    current_object.delete()
                elif new_quantity > current_object.resource.quantity + current_object.quantity:
                    change_form.add_error('new_quantity', 'You cannot assign more resources than available')
                else:
                    current_object.quantity = new_quantity
                    current_object.save()
                change_form = ChangeForm()
            form = ResourceAssignToEmployeeForm()
            form2 = ResourceAssignToProcessForm()

        else:
            form = ResourceAssignToEmployeeForm()
            form2 = ResourceAssignToProcessForm()
            change_form = ChangeForm()

        all_objects = ResourcesAssignedToEmployees.objects.all().order_by('resource__name')
        all_objects2 = ResourcesAssignedToProcess.objects.all().order_by('resource__name')

        self.context['form'] = form
        self.context['form2'] = form2
        self.context['change_form'] = change_form
        self.context['all_objects'] = all_objects
        self.context['all_objects2'] = all_objects2

        return render(request,'resource_mng/assign_resources.html',self.context)
