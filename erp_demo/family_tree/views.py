from django.shortcuts import render
from erp_demo.family_tree.models import FamilyTree


def index(request):
    return render(request, 'family_tree/index.html')


def family_tree(request):
    context = {
        'family_tree': FamilyTree.objects.all(),
    }
    return render(request, 'family_tree/index.html', context)
