from django.contrib import admin

from erp_demo.api.models import ApiTestEmp, ApiTestDep


@admin.register(ApiTestEmp)
class ApiTestEmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'department',)


@admin.register(ApiTestDep)
class ApiTestDepAdmin(admin.ModelAdmin):
    list_display = ('name',)
