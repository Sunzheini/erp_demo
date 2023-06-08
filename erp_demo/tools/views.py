from django.shortcuts import render


def tools_index(request):
    context = {
    }
    return render(request, 'tools/tools_index.html', context)
