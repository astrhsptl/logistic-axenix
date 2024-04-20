from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Warehouse, SalePoint
from product.models import Product


@receiver(post_save, sender=Warehouse)
async def warehouse_update(sender, **kwargs):
    pass
    # need_food = Product.objects.filter(id_warehouse )

@receiver(post_save, sender=SalePoint)
async def sale_point_update(sender, **kwargs):
    pass
    need_food = Product.objects.filter()
class EndpointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'endpoint'