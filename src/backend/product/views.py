from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema


from .models import (
    Category,
    Product,
    Deal,
)
from .serializers import (
    CategoryModelSerializer,
    ProductModelSerializer,
    DealModelSerializer,
)

@extend_schema(tags=['Product'])
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name', 'cost', 'volume', 'weight', 'expiration_date', 'product_quantity', 'id_category', 'id_shipment', 'id_sale_point', 'id_warehouse']


@extend_schema(tags=['Category'])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'name']


@extend_schema(tags=['Deal'])
class DealViewSet(ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealModelSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['id', 'quantity', 'id_sape_point', 'id_product']
