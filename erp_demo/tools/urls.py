from django.urls import path

from erp_demo.tools.views import tools_index, ai_scanner

urlpatterns = [
    path('', tools_index, name='tools index'),
    path('ai-scanner/', ai_scanner, name='ai scanner'),
]
