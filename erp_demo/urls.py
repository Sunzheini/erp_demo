from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('erp_demo.main_app.urls')),
    path('m1/', include('erp_demo.process_mng.urls')),
    path('m2/', include('erp_demo.dox_mng.urls')),
    path('m3/', include('erp_demo.hr_mng.urls')),
]
