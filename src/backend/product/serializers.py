from rest_framework.serializers import ModelSerializer

from .models import (
    Category,
    Product,
    Deal,
)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DealModelSerializer(ModelSerializer):
    class Meta:
        model = Deal
        fields = "__all__"
