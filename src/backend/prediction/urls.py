from django.urls import path

from .views import GategorySalePointSeasonAPI, Season

urlpatterns = [
    path('', Season.as_view(), name='prediction'),
    path('salepoint-category/', GategorySalePointSeasonAPI.as_view(), name='salespoint-category')
]
