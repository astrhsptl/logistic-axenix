from django.db import models

from uuid import uuid4
from django.db import models
from datetime import datetime
from endpoint.models import SalePoint, Warehouse

class Notification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Название')
    description = models.TextField(blank=True)
    is_read = models.BooleanField(default=0, null=False, verbose_name='Прочитано')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')
    id_warehouse = models.ForeignKey(to=Warehouse, null=True, on_delete=models.SET_NULL, related_name='notification')
    id_sale_point = models.ForeignKey(to=SalePoint, null=True, on_delete=models.SET_NULL, related_name='notification')
    def __str__(self):
        return str()

    class Meta:
        ordering = ['created_at', ]