from datetime import date, timedelta

from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from product.models import Deal
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import BadProduct, BestProduct
from .serializers import (
    GategoryinWarehouseSeasonModelSerializer,
    YourRequestSerializerModelSerializer,
)

year_first = year=date.today()-timedelta(days=730)
year_last = year=date.today()-timedelta(days=365)
season = {
    1 : [date(year_first.year, month=12, day=1), date(year_last.year, month=2, day=28)],
    2 : [date(year_last.year, month=3, day=1), date(year_last.year, month=5, day=31)],
    3 : [date(year_last.year, month=6, day=1), date(year_last.year, month=8, day=31)],
    4 : [date(year_last.year, month=9, day=1), date(year_last.year, month=11, day=30)],
}


@extend_schema(
        tags=['Season'],
        request=YourRequestSerializerModelSerializer,
    )
class Season(GenericAPIView):
    def post(self, request):
        season_id = request.data['season_id']
        all_deal_for_season = Deal.objects.filter(created_at__gte=season[season_id][0], created_at__lte=season[season_id][1])
        all_quantity_per_season = Deal.objects.aggregate(Sum("quantity"))
        all_name_products_per_season = set()
        
        for deal in all_deal_for_season:
            all_name_products_per_season.add(deal.id_product.name)
        all_name_products_and_quantity_per_season = {}
        for name_product in list(all_name_products_per_season):
            definite_product = all_deal_for_season.filter(id_product__name=name_product)
            for product in definite_product:
                definite_product_quantity = product.id_product.product_quantity
                if name_product in all_name_products_and_quantity_per_season:
                    all_name_products_and_quantity_per_season[name_product] += definite_product_quantity
                all_name_products_and_quantity_per_season[name_product] = definite_product_quantity
        best_product = BestProduct.objects.create(name = max(all_name_products_and_quantity_per_season))
        bad_product = BadProduct.objects.create(name = min(all_name_products_and_quantity_per_season))
        return Response({'best': best_product.name, 'bad': bad_product.name})

@extend_schema(
        tags=['CategoryWarehouseSeason'],
        request=GategoryinWarehouseSeasonModelSerializer,
    )
class GategorySalePointSeasonAPI(GenericAPIView):
    def post(self, request):
        result = {}
        season_id = request.data['season_id']
        id_sale_point = request.data['id_sale_point']
        all_deal_per_season = Deal.objects.filter(created_at__gte=season[season_id][0], created_at__lte=season[season_id][1])
        all_deal_per_serson_for_sale_point = all_deal_per_season.filter(id_product__id_sale_point=id_sale_point)
        print(all_deal_per_serson_for_sale_point)
        all_quantity_per_season_sale_point = all_deal_per_serson_for_sale_point.aggregate(Sum("quantity"))
        all_categories_per_season_for_sale_point = set()
        for deal in all_deal_per_serson_for_sale_point:
                all_categories_per_season_for_sale_point.add(deal.id_product.id_category.name)
        quantity_per_category= {}
        for category in list(all_categories_per_season_for_sale_point):
            deal_product_in_category = all_deal_per_serson_for_sale_point.filter(id_product__id_category__name=category)
            for quentity in deal_product_in_category:
                if category in quantity_per_category.keys():
                    quantity_per_category[category] += quentity.id_product.product_quantity
                else:
                    quantity_per_category[category] = quentity.id_product.product_quantity
        return Response(quantity_per_category)