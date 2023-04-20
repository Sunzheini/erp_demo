from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.organization_mng.forms import OrgForm, OrgEditForm, OrgDeleteForm, OrgViewForm
from erp_demo.organization_mng.models import Organization


class OrgAppViews:
    @staticmethod
    def org_mng_index(request):
        context = {}
        return render(request, 'organization_mng/org_mng_index.html', context)

    @staticmethod
    def org_list(request):
        template = 'organization_mng/org_list.html'
        all_objects = Organization.objects.all()
        context = {
            'all_objects': all_objects,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def add_org(request):
        template = 'organization_mng/add_org.html'
        if request.method == 'GET':
            form = OrgForm()
        else:
            form = OrgForm(request.POST, request.FILES)
            if form.is_valid():
                output = form.save()  # get the created object
                SupportFunctions.log_info(f"Added an organization `{output.name}`")
                return redirect('org list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def show_org(request, pk, slug):
        template = 'organization_mng/show_org.html'
        org = Organization.objects.filter(pk=pk).get()
        form = OrgViewForm(instance=org)
        context = {
            'form': form,
            'org': org,
        }
        return render(request, template, context)


    @staticmethod
    @SupportFunctions.log_entry(True)
    def edit_org(request, pk, slug):
        template = 'organization_mng/edit_org.html'
        org = Organization.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = OrgEditForm(instance=org)
        else:
            form = OrgEditForm(request.POST, request.FILES, instance=org)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited an organization `{output.name}`")
                return redirect('org list')
        context = {
            'form': form,
            'org': org,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def delete_org(request, pk, slug):
        template = 'organization_mng/delete_org.html'
        org = Organization.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = OrgDeleteForm(instance=org)
        else:
            form = OrgDeleteForm(request.POST, instance=org)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted an organization `{output.name}`")
                return redirect('org list')
        context = {
            'form': form,
            'org': org,
        }
        return render(request, template, context)
