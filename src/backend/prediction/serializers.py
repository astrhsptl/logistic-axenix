from rest_framework import serializers
from rest_framework.serializers import Serializer


class YourRequestSerializerModelSerializer(Serializer):
    season_id = serializers.IntegerField()


class GategoryinWarehouseSeasonModelSerializer(Serializer):
    season_id = serializers.IntegerField()
    id_sale_point  = serializers.UUIDField()

