from rest_framework import serializers

from erp_demo.customer_mng.models import Customer


class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
