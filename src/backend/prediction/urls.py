from django.urls import path
from .views import Season


urlpatterns = [
    path('', Season.as_view(), name='prediction'),
]
