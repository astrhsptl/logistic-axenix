from django.contrib import admin

from .models import (
    Product,
    Category,
    Deal,
)


class ProductAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'cost', 'volume', 'weight', 'expiration_date', 'product_quantity', 'id_category', 'id_shipment', 'id_sale_point', 'id_warehouse'
    )
    list_display = (
        "id",
    )
    search_fields = (
        "id",
    )
    readonly_fields = (
        "id",
    )

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = (
        "id", 'name', 'description'
    )
    list_display = (
        "id",
    )
    search_fields = (
        "id",
    )
    readonly_fields = (
        "id",
    )

admin.site.register(Category, CategoryAdmin)

class DealAdmin(admin.ModelAdmin):
    fields = (
        "id", 'quantity', 'id_sale_point', 'id_product', 'created_at'
    )
    list_display = (
        "id",
    )
    search_fields = (
        "id",
    )
    readonly_fields = (
        "id",
    )

admin.site.register(Deal, DealAdmin)
