from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema


from .models import (
    SalePoint,
    Warehouse,
)
from .serializers import (
    SalePointSerializer,
    WarehouseModelSerializer,
)


@extend_schema(tags=['Warehouse'])
class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'address', 'volume']
    filterset_fields = ['id', 'name', 'address', 'volume']


@extend_schema(tags=['SalePoint'])
class SalePointViewSet(ModelViewSet):
    queryset = SalePoint.objects.all()
    serializer_class = SalePointSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'address', 'volume']
    filterset_fields = ['id', 'name', 'address', 'volume']

