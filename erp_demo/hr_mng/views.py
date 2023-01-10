import random

from django.shortcuts import render


class HrMngViews:
    def __init__(self):
        self.value = 'No info.....'

    def index_view(self, request):
        context = {
            'value': self.value,
        }

        return render(request, 'hr_mng/hr_mng_index.html', context)
