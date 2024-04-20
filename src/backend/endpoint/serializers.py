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

from .models import Associat


class AssociatModelSerializer(ModelSerializer):
    id_warehouse_from = WarehouseModelSerializer(many=True)
    id_warehouse_to = WarehouseModelSerializer(many=True)
    id_sale_point_from = SalePointSerializer(many=True)
    id_sale_point_to = SalePointSerializer(many=True)
    class Meta:
        model = Associat
        fields = ("__all__")
