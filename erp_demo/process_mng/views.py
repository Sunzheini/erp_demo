from django.shortcuts import render


def process_mng_index(request):
    context = {}
    return render(request, 'process_mng/process_mng_index.html', context)
