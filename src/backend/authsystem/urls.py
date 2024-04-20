from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .auth_views import (
    LoginAPIView,
    RefreshAPIView,
    VerifyAPIView,
    ChangePasswordView,
    SupportAPIView,
    UserRegistrationView,
)
from .user_views import UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register_user'),
    path('user/', SupportAPIView.as_view(), name='support'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += router.urls