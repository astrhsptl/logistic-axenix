from uuid import uuid4

from django.db import models
from endpoint.models import (
    SalePoint,
    Warehouse,
)
from logistics.models import Shipment


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, db_index=True, blank=False, null=True, verbose_name='Название')
    cost = models.FloatField(blank=False, null=True, verbose_name='Стоимость')
    volume = models.FloatField(blank=False, null=True, verbose_name='Объем')
    weight = models.FloatField(blank=False, null=True, verbose_name='Вес')
    expiration_date = models.DateField(blank=False, null=True, verbose_name='Срок годности')
    product_quantity = models.IntegerField(blank=False, null=True, verbose_name='Количество')
    id_category = models.ForeignKey(to='Category', related_name='product', on_delete=models.CASCADE)
    id_shipment = models.ForeignKey(to=Shipment, related_name='product', on_delete=models.CASCADE)
    id_sale_point = models.ForeignKey(to=SalePoint, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)
    id_warehouse = models.ForeignKey(to=Warehouse, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)
    
    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self) -> str:
        return self.name


class Deal(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Количество')
    created_at = models.DateField(auto_now_add=True)
    id_sale_point = models.ForeignKey(to=SalePoint, null=True, on_delete=models.SET_NULL, related_name='deal')
    id_product = models.ForeignKey(to=Product, null=True, on_delete=models.SET_NULL, related_name='deal')
    
    def __str__(self) -> str:
        return self.id