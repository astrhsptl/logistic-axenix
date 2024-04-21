from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import BadProduct, BestProduct


class YourRequestSerializerModelSerializer(Serializer):
    season_id = serializers.IntegerField()


# class GategoryinWarehouseSeasonModelSerializer(Serializer):
#     season_id = serializers.IntegerField()
    
class BestProductModelSerializer(ModelSerializer):
    class Meta:
        model = BestProduct
        fields = ['name']


class BadProductModelSerializer(ModelSerializer):
    class Meta:
        model = BadProduct
        fields = ['name']


