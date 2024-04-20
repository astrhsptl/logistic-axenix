from rest_framework.serializers import ModelSerializer
from endpoint.serializers import WarehouseModelSerializer, SalePointSerializer
from .models import (
    Driver,
    Route,
    RouteOrder,
    Shipment,
)


class ShipmentModelSerializer(ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

class RouteOrderModelSerializer(ModelSerializer):
    id_warehouse = WarehouseModelSerializer(many=True)
    id_sape_point = SalePointSerializer(many=True)
    class Meta:
        model = RouteOrder
        fields = "__all__"

class DriverModelSerializer(ModelSerializer):

    class Meta:
        model = Driver
        fields = "__all__"


class RouteModelSerializer(ModelSerializer):
    id_driver = DriverModelSerializer(many=True)
    id_route_order = RouteOrderModelSerializer(many=True)
    class Meta:
        model = Route
        fields = "__all__"