from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet, DealViewSet

router = SimpleRouter()

router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('deal', DealViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
