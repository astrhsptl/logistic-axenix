from datetime import date, timedelta
from os import getenv as env

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv
from notifications.models import Notification
from product.models import Product

load_dotenv()

@receiver(post_save, sender=Product)
def product_update_warehouse_volume(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance)
    warehouse_volume = edit_product.id_warehouse.volume
    all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    for foot_quantity in all_products_for_warehouse:
        product_volume = foot_quantity.volume * foot_quantity.product_quantity
        if product_volume * 100 / warehouse_volume < 50 or product_volume * 100 / warehouse_volume > 80:
            data_for_notification = {'name' : "Заполненность склада",
                                     'description' : f"Склад {edit_product.id_warehouse.name} заполнен на {product_volume * 100 / warehouse_volume}%",
                                    'id_warehouse' : edit_product.id_warehouse}
            notification = Notification.objects.create(**data_for_notification)
            return requests.post(env("URL_WEBSOCKET"), data_for_notification)

# @receiver(post_save, sender=Warehouse)
# async def warehouse_update_less(sender, **kwargs):
#     all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
#     warehouse_volume = sender.volume
#     for need_food in all_products_for_warehouse:
#         product_volume = need_food.volume * need_food.product_quantity
#         if product_volume * 100 / warehouse_volume < 50 or product_volume * 100 / warehouse_volume > 80:
#             data_for_notification = {'name' : "Заполненность склада",
#                                      'description' : f"Склад {sender.name} заполнен на {product_volume * 100 / warehouse_volume}%",
#                                     'id_warehouse' : sender.id}
#             notification = Notification.objects.create(**data_for_notification)
#             serializer = NotificationModelSerializer(notification)
#             if serializer.is_valid():
#                 return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)

@receiver(post_save, sender=Product)
def product_update_warehouse_category(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance)
    all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    all_categories_for_warehouse = set()
    for product in all_products_for_warehouse:
            all_categories_for_warehouse.add(product.id_category.name)
    print(all_categories_for_warehouse)
    quantity_per_category= {}
    for category in list(all_categories_for_warehouse):
        product_in_category = all_products_for_warehouse.filter(id_category__name=category)
        for quentity in product_in_category:
            if category in quantity_per_category:
                quantity_per_category[category] += quentity.product_quantity
            quantity_per_category[category] = quentity.product_quantity
    for category ,quantity_category_product in quantity_per_category:
        if quantity_category_product * 100 / all_products_for_warehouse > 40 or quantity_category_product * 100 / all_products_for_warehouse < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На складе {edit_product.id_warehouse.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_warehouse}",
                                    'id_warehouse': edit_product.id_warehouse}
            notification = Notification.objects.create(**data_for_notification)
            return requests.post(env("URL_WEBSOCKET"), [data_for_notification, quantity_per_category])

# @receiver(post_save, sender=Product)
# async def product_update_ex(sender, **kwargs):
#     all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
#     all_categories_for_warehouse = all_products_for_warehouse.id_category.distinct()
#     quantity_per_category= {}
#     for category in all_categories_for_warehouse:
#         product_in_category = all_products_for_warehouse.filter(id_category=category)
#         for quentity in product_in_category:
#             if category in quantity_per_category:
#                 quantity_per_category[category] += quentity.product_quantity
#             quantity_per_category[category] = quentity.product_quantity
#     for category ,quantity_category_product in quantity_per_category:
#         if quantity_category_product * 100 / all_products_for_warehouse > 40 or quantity_category_product * 100 / all_products_for_warehouse < 10:
#             data_for_notification = {'name' : "Количество продуктов",
#                                      'description' : f"На складе {sender.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_warehouse}",
#                                     'id_warehouse' : sender.id}
#             notification = Notification.objects.create(**data_for_notification)
#             serializer = NotificationModelSerializer(notification)
#             if serializer.is_valid():
#                 return requests.post(env("URL_WEBSOCKET"), {serializer.validated_data, quantity_per_category})

# @receiver(post_save, sender=Warehouse)
# async def product_update(sender, **kwargs):
#     all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
#     all_categories_for_warehouse = all_products_for_warehouse.id_category.distinct()
#     quantity_per_category= {}
#     for category in all_categories_for_warehouse:
#         product_in_category = all_products_for_warehouse.filter(id_category=category)
#         for quentity in product_in_category:
#             if category in quantity_per_category:
#                 quantity_per_category[category] += quentity.product_quantity
#             quantity_per_category[category] = quentity.product_quantity
#     for category ,quantity_category_product in quantity_per_category:
#         if quantity_category_product * 100 / all_products_for_warehouse > 40 or quantity_category_product * 100 / all_products_for_warehouse < 10:
#             data_for_notification = {'name' : "Количество продуктов",
#                                      'description' : f"На складе {sender.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_warehouse}",
#                                     'id_warehouse' : sender.id}
#             notification = Notification.objects.create(**data_for_notification)
#             serializer = NotificationModelSerializer(notification)
#             if serializer.is_valid():
#                 return requests.post(env("URL_WEBSOCKET"), {serializer.validated_data, quantity_per_category})

@receiver(post_save, sender=Product)
def product_update_warehouse_expensive(sender, instance, created,  **kwargs):
    edit_product = Product.objects.get(id=instance)
    all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    all_expiration_date_for_warehouse = all_products_for_warehouse.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_warehouse in all_expiration_date_for_warehouse:
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {edit_product.id_warehouse.name.name} у товара {expiration_product_for_warehouse.name} срок годности истекает через {expiration_product_for_warehouse.expiration_date-date.today()} дней',
                                'id_warehouse': edit_product.id_warehouse}
        notification = Notification.objects.create(**data_for_notification)
        return requests.post(env("URL_WEBSOCKET"), data_for_notification)

# @receiver(post_save, sender=Warehouse)
# async def warehouse_update(sender, **kwargs):
#     all_products_for_warehouse = Product.objects.filter(id_warehouse=sender.id)
#     all_expiration_date_for_warehouse = all_products_for_warehouse.filter(expiration_date__lte=date.today() + timedelta(days=2))
#     for expiration_product_for_warehouse in all_expiration_date_for_warehouse:
#         data_for_notification = {'name' : "Качество товара",
#                                 'description' : f'На складе {sender.name} у товара {expiration_product_for_warehouse.name} срок годности истекает через {expiration_product_for_warehouse.expiration_date-date.today()} дней'}
#         notification = Notification.objects.create(**data_for_notification)
#         serializer = NotificationModelSerializer(notification)
#         if serializer.is_valid():
#             return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)


@receiver(post_save, sender=Product)
def product_update_sale_point_volume(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance)
    all_products_for_sale_point = Product.objects.filter(id_sale_point=edit_product.id_sale_point)
    sale_point_volume = edit_product.id_warehouse.volume
    for foot_quantity in all_products_for_sale_point:
        product_volume = foot_quantity.volume * foot_quantity.product_quantity
        if product_volume * 100 / sale_point_volume < 50 or product_volume * 100 / sale_point_volume > 75:
            data_for_notification = {'name' : "Заполненность торговой точки",
                                     'description' : f"Торговая точка {edit_product.id_sale_point.name} заполнена на {product_volume * 100 / sale_point_volume}%",
                                    'id_sale_point' : edit_product.id_sale_point}
            notification = Notification.objects.create(**data_for_notification)
            return requests.post(env("URL_WEBSOCKET"), data_for_notification)

@receiver(post_save, sender=Product)
def product_update_warehouse_category(sender, **kwarg):
    return requests.post(env("URL_WEBSOCKET"), json={
  "id": "string",
  "name": "string",
  "description": "string",
  "is_read": True,
  "created_at": "string",
  "id_warehouse": "string",
  "id_sale_point": "string"
})

@receiver(post_save, sender=Product)
def product_update_warehouse_category(sender, instance, created, **kwarg):
    edit_product = Product.objects.get(id=instance)
    all_products_for_sale_point = Product.objects.filter(id_warehouse=edit_product.id_sale_point)
    all_categories_for_sale_point = set()
    for product in all_products_for_sale_point:
            all_categories_for_sale_point.add(product.id_category.name)
    quantity_per_category= {}
    for category in all_categories_for_sale_point:
        product_in_category = all_products_for_sale_point.filter(id_category__name=category)
        for quentity in product_in_category:
            if category in quantity_per_category:
                quantity_per_category[category] += quentity.product_quantity
            quantity_per_category[category] = quentity.product_quantity
    for quantity_category_product in quantity_per_category.values():
        if quantity_category_product * 100 / all_products_for_sale_point > 40 or quantity_category_product * 100 / all_products_for_sale_point < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На торговой точке {edit_product.id_sale_point.name} категория {category} состовляет {quantity_category_product * 100 / all_products_for_sale_point}",
                                    'id_sale_point' : edit_product.id_sale_point}
            notification = Notification.objects.create(**data_for_notification)
            return requests.post(env("URL_WEBSOCKET"), [data_for_notification, quantity_per_category])


@receiver(post_save, sender=Product)
async def product_update_warehouse_expensive(sender, instance **kwargs):
    all_products_for_sale_point = Product.objects.filter(id_warehouse=sender.id)
    all_expiration_date_for_sale_point = all_products_for_sale_point.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_sale_point in all_expiration_date_for_sale_point:
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {sender.name} у товара {expiration_product_for_sale_point.name} срок годности истекает через {expiration_product_for_sale_point.expiration_date-date.today()} дней'}
        notification = Notification.objects.create(**data_for_notification)
        serializer = NotificationModelSerializer(notification)
        if serializer.is_valid():
            return requests.post(env("URL_WEBSOCKET"), serializer.validated_data)
