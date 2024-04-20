from rest_framework.routers import SimpleRouter
from .views import WarehouseViewSet, SalePointViewSet, AssociatViewSet
router = SimpleRouter()

router.register('warehouse', WarehouseViewSet)
router.register('salepoint', SalePointViewSet)
router.register('associate', AssociatViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls