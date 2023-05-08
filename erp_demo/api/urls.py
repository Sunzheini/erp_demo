from django.urls import path, include

from erp_demo.api.views import ApiTestEmpListView, ApiTestDepListView, DemoApiView, IndexView

urlpatterns = [
    # http://127.0.0.1:8000/api/employees/
    path('employees/', ApiTestEmpListView.as_view(), name='api list employees'),
    # http://127.0.0.1:8000/api/departments/
    path('departments/', ApiTestDepListView.as_view(), name='api list departments'),
    # http://127.0.0.1:8000/api/demo/
    path('demo/', DemoApiView.as_view(), name='demo view'),
    # http://127.0.0.1:8000/api/
    path('', IndexView.as_view(), name='api index'),

    path('employees/', ApiTestEmpListView.as_view(), name='api list employees'),
]
