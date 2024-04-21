from uuid import uuid4

from django.db import models
from endpoint.models import SalePoint


class SalePointCategory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    id_sale_point = models.ForeignKey(to=SalePoint, null=True, related_name='season', on_delete=models.SET_NULL)

class BestProduct(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
    date = models.DateField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.name

class BadProduct(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
    date = models.DateField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.name

