from turtle import distance
from uuid import uuid4

from django.db import models

class Warehouse(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=True, verbose_name='Название')
    address = models.CharField(max_length=256, blank=False, null=True, db_index=True, verbose_name='Адрес')
    volume = models.FloatField(blank=False, null=True, verbose_name='Объем')
    is_provider = models.BooleanField(blank=False, null=True, default=0, verbose_name='Поставщик')
    lon = models.FloatField(blank=False, null=True, verbose_name='Долгота')
    lat = models.FloatField(blank=False, null=True, verbose_name='Широта')
    
    def __str__(self) -> str:
        return self.address


class SalePoint(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=True, verbose_name='Название')
    address = models.CharField(max_length=256, blank=False, null=True, db_index=True, verbose_name='Адрес')
    volume = models.FloatField(blank=False, null=True, verbose_name='Объем')
    lon = models.FloatField(blank=False, null=True, verbose_name='Долгота')
    lat = models.FloatField(blank=False, null=True, verbose_name='Широта')
    
    def __str__(self) -> str:
        return self.address


class Associat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    id_warehouse_from = models.ForeignKey(to=Warehouse, blank=True, null=True, related_name='associat_rout', on_delete=models.SET_NULL)
    id_warehouse_to = models.ForeignKey(to=Warehouse, blank=True, null=True, on_delete=models.SET_NULL)
    id_sale_point_from = models.ForeignKey(to=SalePoint, blank=True, null=True, related_name='associat_rout', on_delete=models.SET_NULL)
    id_sale_point_to = models.ForeignKey(to=SalePoint, blank=True, null=True, on_delete=models.SET_NULL)
    distance = models.IntegerField(blank=False, null=False, verbose_name='Дистанция')
    duration = models.IntegerField(blank=False, null=False, verbose_name='Время в секундах')
