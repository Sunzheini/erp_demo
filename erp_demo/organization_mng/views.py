from django.shortcuts import render, redirect


class OrgAppViews:
    @staticmethod
    def index(request):
        template = 'organization_mng/organization_mng_index.html'

        context = {

        }
        return render(request, template, context)
