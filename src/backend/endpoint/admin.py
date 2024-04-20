from django.contrib import admin

from .models import (
    Warehouse,
    SalePoint)


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