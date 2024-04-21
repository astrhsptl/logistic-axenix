import copy
from datetime import date, timedelta
from os import getenv as env
from uuid import uuid4

import requests
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv
from endpoint.models import (
    SalePoint,
    Warehouse,
)
from logistics.models import Shipment

load_dotenv()
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


@receiver(post_save, sender=Product)
def product_update_warehouse_volume(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_warehouse is None:
        return 
    print(edit_product)
    warehouse_volume = edit_product.id_warehouse.volume
    print(warehouse_volume)
    all_products_for_warehouse: models.BaseManager[Product] = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    print(all_products_for_warehouse)
    for food_quantity in all_products_for_warehouse:
        print(food_quantity)
        product_volume = food_quantity.volume * food_quantity.product_quantity
        print(product_volume)
        if product_volume * 100 / warehouse_volume < 50 or product_volume * 100 / warehouse_volume > 80:
            print(product_volume * 100 / warehouse_volume < 50)
            print(product_volume * 100 / warehouse_volume > 80)
            data_for_notification = {'name' : "Заполненность склада",
                                     'description' : f"Склад {edit_product.id_warehouse.name} заполнен на {product_volume * 100 / warehouse_volume}%"}
            print(data_for_notification)
            return requests.post(env("URL_WEBSOCKET"), json=data_for_notification)


@receiver(post_save, sender=Product)
def product_update_warehouse_category(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_warehouse is None:
        return 
    print(edit_product)
    all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    print(all_products_for_warehouse)
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
    all_quentity = all_products_for_warehouse.aggregate(all=Sum('product_quantity'))
    print(all_quentity)
    for category ,quantity_category_product in quantity_per_category.items():
        if quantity_category_product * 100 / all_quentity['all'] > 40 or quantity_category_product * 100 / all_quentity['all'] < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На складе {edit_product.id_warehouse.name} категория {category} состовляет {quantity_category_product * 100 / all_quentity['all']}"}
            return requests.post(env("URL_WEBSOCKET"), json=data_for_notification)

@receiver(post_save, sender=Product)
def product_update_warehouse_expensive(sender, instance, created,  **kwargs):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_warehouse is None:
        return 
    all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    all_expiration_date_for_warehouse = all_products_for_warehouse.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_warehouse in all_expiration_date_for_warehouse:
        print(date.today())
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {edit_product.id_warehouse.name} у товара {expiration_product_for_warehouse.name} срок годности истекает через {expiration_product_for_warehouse.expiration_date-date.today()} дней'}
        return requests.post(env("URL_WEBSOCKET"), json=data_for_notification)


@receiver(post_save, sender=Product)
def product_update_sale_point_volume(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_sale_point is None:
        return 
    all_products_for_sale_point = Product.objects.filter(id_sale_point=edit_product.id_sale_point)
    sale_point_volume = edit_product.id_sale_point.volume
    print(sale_point_volume)
    for food_quantity in all_products_for_sale_point:
        product_volume = food_quantity.volume * food_quantity.product_quantity
        print(product_volume)
        if product_volume * 100 / sale_point_volume < 50 or product_volume * 100 / sale_point_volume > 75:
            data_for_notification = {'name' : "Заполненность торговой точки",
                                     'description' : f"Торговая точка {edit_product.id_sale_point.name} заполнена на {product_volume * 100 / sale_point_volume}%"}
            return requests.post(env("URL_WEBSOCKET"), json=data_for_notification)

# @receiver(post_save, sender=Product)
# def product(sender, *args, **kwarg):
#     print('xyi')
#     return requests.post(env("URL_WEBSOCKET"), json={
#   "id": "string",
#   "name": "string",
#   "description": "string",
#   "is_read": True,
#   "created_at": "string",
#   "id_warehouse": "string",
#   "id_sale_point": "string"
# })


@receiver(post_save, sender=Product)
def product_update_sale_point_category(sender, instance, created, **kwarg):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_sale_point is None:
        return 
    all_products_for_sale_point = Product.objects.filter(id_sale_point=edit_product.id_sale_point)
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
    quantity_websocket = copy.deepcopy(quantity_per_category)
    print(quantity_websocket)
    all_quentity = all_products_for_sale_point.aggregate(all=Sum('product_quantity'))
    for quantity_category_product in quantity_per_category.values():
        if quantity_category_product * 100 / all_quentity['all'] > 40 or quantity_category_product * 100 / all_quentity['all'] < 10:
            data_for_notification = {'name' : "Количество продуктов",
                                     'description' : f"На торговой точке {edit_product.id_sale_point.name} категория {category} состовляет {quantity_category_product * 100 / all_quentity['all']}"}
            # notification = Notification.objects.create(**data_for_notification)
            requests.post(env("URL_WEBSOCKET"), json=data_for_notification)


@receiver(post_save, sender=Product)
def product_update_sale_point_expensive(sender, instance, created, **kwargs):
    edit_product = Product.objects.get(id=instance.id)
    if edit_product.id_sale_point is None:
        return 
    all_products_for_sale_point = Product.objects.filter(id_sale_point=edit_product.id_sale_point)
    all_expiration_date_for_sale_point = all_products_for_sale_point.filter(expiration_date__lte=date.today() + timedelta(days=2))
    for expiration_product_for_sale_point in all_expiration_date_for_sale_point:
        data_for_notification = {'name' : "Качество товара",
                                'description' : f'На складе {edit_product.id_sale_point.name} у товара {expiration_product_for_sale_point.name} срок годности истекает через {expiration_product_for_sale_point.expiration_date-date.today()} дней'}
        print(data_for_notification)
        requests.post(env("URL_WEBSOCKET"), json=data_for_notification)

    # edit_product = Product.objects.get(id=instance.id)
    # if edit_product.id_warehouse is None:
    #     return 
    # all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
    # all_expiration_date_for_warehouse = all_products_for_warehouse.filter(expiration_date__lte=date.today() + timedelta(days=2))
    # for expiration_product_for_warehouse in all_expiration_date_for_warehouse:
    #     print(date.today())
    #     data_for_notification = {'name' : "Качество товара",
    #                             'description' : f'На складе {edit_product.id_warehouse.name} у товара {expiration_product_for_warehouse.name} срок годности истекает через {expiration_product_for_warehouse.expiration_date-date.today()} дней'}
    #     return requests.post(env("URL_WEBSOCKET"), json=data_for_notification)
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
    created_at = models.DateField(auto_now_add=False, auto_now=False)
    id_sale_point = models.ForeignKey(to=SalePoint, null=True, on_delete=models.SET_NULL, related_name='deal')
    id_product = models.ForeignKey(to=Product, null=True, on_delete=models.SET_NULL, related_name='deal')