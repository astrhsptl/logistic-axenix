from django.contrib import admin

from .models import (
    Driver,
    Shipment,
    Route,
    RouteOrder,
)

class DriverAdmin(admin.ModelAdmin):
    fields = (
        "id", 'first_name', 'last_name', 'phone', 'experience', 'volume', 'user_id'
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

admin.site.register(Driver, DriverAdmin)


class RouteAdmin(admin.ModelAdmin):
    fields = (
        "id", 'name', 'id_driver'
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

admin.site.register(Route, RouteAdmin)


class RouteOrderAdmin(admin.ModelAdmin):
    fields = (
        "id", 'order_position', 'complited', 'id_warehouse', 'id_salepoint', 'id_route'
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

admin.site.register(RouteOrder, RouteOrderAdmin)


class ShipmentAdmin(admin.ModelAdmin):
    fields = (
        "id", 'name'
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

admin.site.register(Shipment, ShipmentAdmin)