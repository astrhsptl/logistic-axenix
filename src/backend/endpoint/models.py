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