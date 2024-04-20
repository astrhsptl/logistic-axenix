from rest_framework.routers import SimpleRouter
from .views import WarehouseViewSet, SalePointViewSet
router = SimpleRouter()

router.register('warehouse', WarehouseViewSet)
router.register('salepoint', SalePointViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls