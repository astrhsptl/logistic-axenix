from rest_framework import serializers

from .models import BestProduct, BadProduct

from rest_framework.serializers import ModelSerializer, Serializer


class YourRequestSerializerModelSerializer(Serializer):
    season_id = serializers.IntegerField()


class BestProductModelSerializer(ModelSerializer):
    class Meta:
        model = BestProduct
        fields = ['name']


class BadProductModelSerializer(ModelSerializer):
    class Meta:
        model = BadProduct
        fields = ['name']
