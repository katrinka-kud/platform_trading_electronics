from rest_framework.serializers import ModelSerializer

from main.models import SupplierNetwork, Product


class SupplierNetworkSerializer(ModelSerializer):
    class Meta:
        model = SupplierNetwork
        fields = '__all__'

    def update(self, instance, validated_data):
        """
        Удаляет 'debt_to_supplier' из validated_data, если он присутствует.
        """
        validated_data.pop('debt_to_supplier', None)
        return super().update(instance, validated_data)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
