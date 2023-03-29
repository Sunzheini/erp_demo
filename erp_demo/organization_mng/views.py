from django.shortcuts import render, redirect

from erp_demo.organization_mng.forms import CreateOrgForm
from erp_demo.organization_mng.models import Organization


class OrgAppViews:
    @staticmethod
    def index(request):
        template = 'organization_mng/organization_mng_index.html'

        if request.method == 'GET':
            form = CreateOrgForm()
        else:
            form = CreateOrgForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('org list')

        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def org_list(request):
        template = 'organization_mng/organizations_list.html'

        all_organizations = Organization.objects.all()

        context = {
            'all_organizations': all_organizations,
        }
        return render(request, template, context)
