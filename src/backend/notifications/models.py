from django.db import models

from uuid import uuid4
from django.db import models

from backend.endpoint.models import SalePoint, Warehouse


class Notification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Название')
    description = models.TextField(blank=True)
    id_warehouse = models.ForeignKey(to=Warehouse, null=True, on_delete=models.SET_NULL, related_name='notification')
    id_sale_point = models.ForeignKey(to=SalePoint, null=True, on_delete=models.SET_NULL, related_name='notification')
    def __str__(self):
        return str()
