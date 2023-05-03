from django.db import models


class ApiTestDep(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name


class ApiTestEmp(models.Model):
    name = models.CharField(max_length=30,)
    salary = models.PositiveIntegerField()
    department = models.ForeignKey(ApiTestDep, on_delete=models.RESTRICT,)

    def __str__(self):
        return self.name
