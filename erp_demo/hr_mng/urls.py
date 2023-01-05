from django.urls import path, include

from erp_demo.hr_mng.views import hr_mng_index

urlpatterns = [
    path('', hr_mng_index, name='hr mng index'),
]
