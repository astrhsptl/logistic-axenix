from django.contrib import admin

from .models import (
    Warehouse,
    SalePoint)

from django.contrib import admin

from .models import Associat


class AssociatAdmin(admin.ModelAdmin):
    fields = (
        "id", 'distance', 'duration', 'id_warehouse_from', 
                    'id_warehouse_to', 
                    'id_sale_point_from', 
                    'id_sale_point_to'
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

admin.site.register(Associat, AssociatAdmin)

class WarehouseAdmin(admin.ModelAdmin):
    fields = (
        "id", 'name', 'address', 'volume', 'is_provider', 'lon', 'lat'
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

admin.site.register(Warehouse, WarehouseAdmin)

class SalePointAdmin(admin.ModelAdmin):
    fields = (
        "id", 'name', 'address', 'volume', 'lon', 'lat'
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

admin.site.register(SalePoint, SalePointAdmin)