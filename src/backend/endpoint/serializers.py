from rest_framework.serializers import ModelSerializer

from .models import (
    SalePoint,
    Warehouse,
)


class WarehouseModelSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ("__all__", )


class SalePointSerializer(ModelSerializer):
    class Meta:
        model = SalePoint
        fields = ("__all__", )