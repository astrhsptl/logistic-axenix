from rest_framework.serializers import ModelSerializer

from .models import (
    Driver,
    Route,
    RouteOrder,
    Shipment,
)


class DriverModelSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ("__all__", )


class RouteModelSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = ("__all__", )


class RouteOrderModelSerializer(ModelSerializer):
    class Meta:
        model = RouteOrder
        fields = ("__all__", )


class ShipmentModelSerializer(ModelSerializer):
    class Meta:
        model = Shipment
        fields = ("__all__", )
