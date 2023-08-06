from django.urls import path, include

from erp_demo.api.views import ApiEmployeesView, IndexView

urlpatterns = [
    # http://127.0.0.1:8000/api/
    path('', IndexView.as_view(), name='api index'),

    # http://127.0.0.1:8000/api/employees/
    path('employees/', ApiEmployeesView.as_view(), name='api list employees'),
]
