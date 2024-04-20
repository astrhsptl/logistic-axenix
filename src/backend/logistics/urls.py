from rest_framework.routers import SimpleRouter
from .views import DriverViewSet, RouteViewSet, RouteOrderViewSet, ShipmentViewSet

router = SimpleRouter()

router.register('driver', DriverViewSet)
router.register('route', RouteViewSet)
router.register('route_order', RouteOrderViewSet)
router.register('shipment', ShipmentViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls