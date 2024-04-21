from datetime import date, timedelta

from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from product.models import Deal
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import BadProduct, BestProduct
from .serializers import (
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

# @extend_schema(
#         tags=['CategoryWarehouseSeason'],
#         request=YourRequestSerializerModelSerializer,
#     )
# class Gategory_in_Warehouse_SeasonAPI(GenericAPIView):
#     def post(self, request):
#         result = {}
#         season_id = request.data['season_id']
#         id_warehouse = request.data['id_warehouse']
#         all_deal_for_season = Deal.objects.filter(created_at__gte=season[season_id][0], created_at__lte=season[season_id][1])
#         x = all_deal_for_season.id_product.filter(id_warehouse=id_warehouse)
#         print(x)
#         all_quantity_per_season = Deal.objects.aggregate(Sum("quantity"))
#         all_name_products_per_season = set()
#         for deal in all_deal_for_season:
#             all_name_products_per_season.add(deal.id_product.name)
#         all_name_products_and_quantity_per_season = {}
#         for name_product in list(all_name_products_per_season):
#             definite_product = all_deal_for_season.filter(id_product__name=name_product)
#             for product in definite_product:
#                 definite_product_quantity = product.id_product.product_quantity
#                 if name_product in all_name_products_and_quantity_per_season:
#                     all_name_products_and_quantity_per_season[name_product] += definite_product_quantity
#                 all_name_products_and_quantity_per_season[name_product] = definite_product_quantity
#         best_product = BestProduct.objects.create(name = max(all_name_products_and_quantity_per_season))
#         bad_product = BadProduct.objects.create(name = min(all_name_products_and_quantity_per_season))

#         id_warehouse = request.data['id_warehouse']
#         all_products_for_warehouse = Product.objects.filter(id_warehouse=edit_product.id_warehouse)
#         print(all_products_for_warehouse)
#         all_categories_for_warehouse = set()
#         for product in all_products_for_warehouse:
#                 all_categories_for_warehouse.add(product.id_category.name)
#         print(all_categories_for_warehouse)
#         quantity_per_category= {}
#         for category in list(all_categories_for_warehouse):
#             product_in_category = all_products_for_warehouse.filter(id_category__name=category)
#             for quentity in product_in_category:
#                 if category in quantity_per_category:
#                     quantity_per_category[category] += quentity.product_quantity
#                 quantity_per_category[category] = quentity.product_quantity
