from django.shortcuts import render


class OperationsAppViews:
    def __init__(self):
        self.context = {}

    def index(self, request):
        try:
            return render(request, 'operations_mng/operations_mng_index.html', self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})
