from django.urls import path

from erp_demo.tools.views import ToolsMngViews

urlpatterns = [
    path('generate_system_checklist/',
         ToolsMngViews().generate_system_checklist, name='generate system checklist'),
]
