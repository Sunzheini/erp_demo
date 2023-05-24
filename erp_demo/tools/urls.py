from django.urls import path

from erp_demo.tools.views import tools_index

urlpatterns = [
    path('', tools_index, name='tools index'),
]
