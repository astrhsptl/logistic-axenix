from uuid import uuid4

from django.db import models
from authsystem.models import User
from endpoint.models import (
    SalePoint,
    Warehouse,
)


class Shipment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name='Название')
    
    def __str__(self) -> str:
        return self.name


class Route(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    # provider_warehouse = models.BooleanField(blank=False, null=False, )
    id_driver = models.ForeignKey(to='Driver', null=True, on_delete=models.SET_NULL, related_name='route')
    
    def __str__(self) -> str:
        return self.id


class Driver(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Фамилия')
    phone = models.IntegerField(null=False, blank=False, verbose_name='Телефон')
    experience = models.IntegerField(blank=False, default=0, null=False, verbose_name='Стаж')
    volume = models.FloatField(blank=False, null=True, verbose_name='Объем')
    user_id = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, blank=True, related_name='driver')
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class RouteOrder(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    order_position = models.IntegerField(blank=False, null=False, )
    complited = models.BooleanField(blank=False, null=False, default=False, verbose_name='Состояние')
    id_warehouse = models.ForeignKey(to=Warehouse, null=True, on_delete=models.SET_NULL, related_name='route_order')
    id_salepoint = models.ForeignKey(to=SalePoint, null=True, on_delete=models.SET_NULL, related_name='route_order')
    id_route = models.ForeignKey(to='Route', on_delete=models.PROTECT, related_name='route_order')
    
    def __str__(self) -> str:
        return self.id
