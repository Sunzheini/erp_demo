from django.shortcuts import render


def index(request):
    return render(request, 'family_tree/index.html')
