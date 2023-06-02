from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),

    path('', include('erp_demo.main_app.urls')),
    path('m0/', include('erp_demo.organization_mng.urls')),
    path('m1/', include('erp_demo.process_mng.urls')),
    path('m2/', include('erp_demo.dox_mng.urls')),
    path('m3/', include('erp_demo.hr_mng.urls')),
    path('m4/', include('erp_demo.customer_mng.urls')),
    path('m5/', include('erp_demo.supplier_mng.urls')),
    path('m6/', include('erp_demo.tools.urls')),
    path('m7/', include('erp_demo.kpi_mng.urls')),
    path('m8/', include('erp_demo.risk_mng.urls')),
    path('m9/', include('erp_demo.opportunity_mng.urls')),

    path('users/', include('erp_demo.user_mng.urls')),

    path('api-auth/', include('rest_framework.urls')),  # enable the browsable API
    path('api/', include('erp_demo.api.urls')),
]
