from rest_framework.serializers import ModelSerializer

from .models import (
    SalePoint,
    Warehouse,
    Associat,
)


class WarehouseModelSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class SalePointSerializer(ModelSerializer):
    class Meta:
        model = SalePoint
        fields = "__all__" 


class AssociatModelSerializer(ModelSerializer):
    warehouse_from = WarehouseModelSerializer(read_only=True)
    warehouse_to = WarehouseModelSerializer(read_only=True)
    sale_point_from = SalePointSerializer(read_only=True)
    sale_point_to = SalePointSerializer(read_only=True)
    class Meta:
        model = Associat
        fields = ("__all__")
        extra_kwargs = {
            'id_warehouse_from': {'required': False},
            "id_warehouse_to": {'required': False},
            'id_sale_point_from': {'required': False},
            'id_sale_point_to' : {'required': False},
        } 
