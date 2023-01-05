from django.shortcuts import render


def hr_mng_index(request):
    context = {}
    return render(request, 'hr_mng/hr_mng_index.html', context)
