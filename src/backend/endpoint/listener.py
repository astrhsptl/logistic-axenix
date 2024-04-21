from os import name
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from os import getenv as env
from dotenv import load_dotenv
from backend.notifications.apps import NotificationsConfig
from .models import Warehouse, SalePoint
from product.models import Product
from notifications.models import Notification
from datetime import date, timedelta
from notifications.serializers import NotificationModelSerializer

load_dotenv()

@receiver(post_save, sender=Warehouse)
async def warehouse_update_less(sender, **kwargs):
    all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
    warehouse_volume = sender.volume
    for need_food in all_products_for_warehouse:
        product_volume = need_food.volume * need_food.product_quantity
        if product_volume * 100 / warehouse_volume < 50 or product_volume * 100 / warehouse_volume > 80:
            data_for_notification = {'name' : "Заполненность склада",
                                     'description' : f"Склад {sender.name} заполнен на {product_volume * 100 / warehouse_volume}%",
                                    'id_warehouse' : sender.id}
            notification = Notification.objects.create(**data_for_notification)
            serializer = NotificationModelSerializer(notification)
            if serializer.is_valid():
                return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)


@receiver(post_save, sender=Warehouse)
async def warehouse_update(sender, **kwargs):
    all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
    all_categories_for_warehouse = all_products_for_warehouse.id_category.distinct()
    quantity_per_category= {}
    for category in all_categories_for_warehouse:
        product_in_category = all_products_for_warehouse.filter(id_category=category)
        for quentity in product_in_category:
            if category in quantity_per_category:
                quantity_per_category[category] += quentity.product_quantity
            quantity_per_category[category] = quentity.product_quantity
    for category ,quantity_category_product in quantity_per_category:
        if quantity_category_product * 100 / all_products_for_warehouse > 40 or quantity_category_product * 100 / all_products_for_warehouse < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На складе {sender.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_warehouse}",
                                    'id_warehouse' : sender.id}
            notification = Notification.objects.create(**data_for_notification)
            serializer = NotificationModelSerializer(notification)
            if serializer.is_valid():
                return requests.post(env("URL_WEBSOCKET"), {serializer.validated_data, quantity_per_category})


@receiver(post_save, sender=Warehouse)
async def warehouse_update(sender, **kwargs):
    all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
    all_expiration_date_for_warehouse = all_products_for_warehouse.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_warehouse in all_expiration_date_for_warehouse:
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {sender.name} у товара {expiration_product_for_warehouse.name} срок годности истекает через {expiration_product_for_warehouse.expiration_date-date.today()} дней'}
        notification = Notification.objects.create(**data_for_notification)
        serializer = NotificationModelSerializer(notification)
        if serializer.is_valid():
            return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)


@receiver(post_save, sender=SalePoint)
async def sale_point_update(sender, **kwargs):
    all_products_for_sale_point = Product.objects.filter(id_sale_point=sender.id)
    sale_point_volume = sender.volume
    for need_food in all_products_for_sale_point:
        product_volume = need_food.volume * need_food.product_quantity
        if product_volume * 100 / sale_point_volume < 50 or product_volume * 100 / sale_point_volume > 75:
            data_for_notification = {'name' : "Заполненность торговой точки",
                                     'description' : f"Торговая точка {sender.name} заполнена на {product_volume * 100 / sale_point_volume}%",
                                    'id_warehouse' : sender.id}
            notification = Notification.objects.create(**data_for_notification)
            serializer = NotificationModelSerializer(notification)
            if serializer.is_valid():
                return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)


@receiver(post_save, sender=SalePoint)
async def sale_point_update(sender, **kwargs):
    all_products_for_sale_point = Product.objects.filter(id_warehouse=sender.id)
    all_categories_for_sale_point = []
    for category in all_products_for_sale_point:
            all_categories_for_sale_point = category.id_product__name.distinct()
    quantity_per_category= {}
    for category in all_categories_for_sale_point:
        product_in_category = all_products_for_sale_point.filter(id_category=category)
        for quentity in product_in_category:
            if category in quantity_per_category:
                quantity_per_category[category] += quentity.product_quantity
            quantity_per_category[category] = quentity.product_quantity
    for quantity_category_product in quantity_per_category.values():
        if quantity_category_product * 100 / all_products_for_sale_point > 40 or quantity_category_product * 100 / all_products_for_sale_point < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На торговой точке {sender.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_sale_point}",
                                    'id_warehouse' : sender.id}
            notification = Notification.objects.create(**data_for_notification)
            serializer = NotificationModelSerializer(notification)
            if serializer.is_valid():
                return requests.post(env("URL_WEBSOCKET"), {serializer.validated_data, quantity_per_category})


@receiver(post_save, sender=Warehouse)
async def sale_point_update(sender, **kwargs):
    all_products_for_sale_point = Product.objects.filter(id_warehouse=sender.id)
    all_expiration_date_for_sale_point = all_products_for_sale_point.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_sale_point in all_expiration_date_for_sale_point:
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {sender.name} у товара {expiration_product_for_sale_point.name} срок годности истекает через {expiration_product_for_sale_point.expiration_date-date.today()} дней'}
        notification = Notification.objects.create(**data_for_notification)
        serializer = NotificationModelSerializer(notification)
        if serializer.is_valid():
            return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)
