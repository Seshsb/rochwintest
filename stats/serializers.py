from .models import Client, Employee, Product, Order, OrderM2M
from rest_framework import serializers


class ClientResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    products_count = serializers.IntegerField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EmployeeResultSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    clients_count = serializers.IntegerField()
    products_count = serializers.IntegerField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)

