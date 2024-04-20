from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema


from .models import (
    Driver,
    Route,
    RouteOrder,
    Shipment,
)
from .serializers import (
    DriverModelSerializer,
    RouteModelSerializer,
    RouteOrderModelSerializer,
    ShipmentModelSerializer,
)

@extend_schema(tags=['Driver'])
class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'last_name', 'user_id']

@extend_schema(tags=['Route'])
class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'id_driver']

@extend_schema(tags=['RouteOrder'])
class RouteOrderViewSet(ModelViewSet):
    queryset = RouteOrder.objects.all()
    serializer_class = RouteOrderModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'id_warehouse', 'id_salepoint', 'id_route']

@extend_schema(tags=['Shipment'])
class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name']

