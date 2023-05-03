from rest_framework import serializers

from erp_demo.api.models import ApiTestEmp, ApiTestDep


# Short
# -----------------------------------------------------------------------
class ShortApiTestEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTestEmp
        fields = ('id', 'name',)


# python object to json, ModelSerializer is like ModelForm
class ShortApiTestDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTestDep
        fields = '__all__'


# Detailed
# -----------------------------------------------------------------------

class ApiTestDepSerializer(serializers.ModelSerializer):
    # naming is model name.lower() + set
    apitestemp_set = ShortApiTestEmpSerializer(many=True)
    # many=True means there are many ApiTestEmp objects in ApiTestDep
    # same is for many-to-many field relationship

    class Meta:
        model = ApiTestDep
        fields = '__all__'


class ApiTestEmpSerializer(serializers.ModelSerializer):
    # on department not only show the id but all dep info
    department = ShortApiTestDepSerializer()

    class Meta:
        model = ApiTestEmp
        fields = '__all__'

    # override create method to be able to create new employee (because of relation with department)
    def create(self, validated_data):
        department_name = validated_data.pop('department').get('name')
        try:
            department = ApiTestDep.objects.filter(name=department_name).get()
        except ApiTestDep.DoesNotExist:
            department = ApiTestDep.objects.create(name=department_name)
        return ApiTestEmp.objects.create(department=department, **validated_data)


# Custom
# -----------------------------------------------------------------------

class NameSerializer(serializers.Serializer):
    name = serializers.CharField()    # name is the property of the model


class DemoSerializer(serializers.Serializer):
    employees = ShortApiTestEmpSerializer(many=True)
    departments = ShortApiTestDepSerializer(many=True)

    #custom data
    employees_count = serializers.IntegerField()
    first_department = serializers.CharField()
    department_names = NameSerializer(many=True)    # nested serializer
