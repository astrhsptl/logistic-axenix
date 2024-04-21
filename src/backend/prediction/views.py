from os import name
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema
from django.db.models import Sum
from .models import BadProduct, BestProduct
from product.models import Deal
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from .serializers import YourRequestSerializerModelSerializer
from rest_framework.response import Response


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
        # return Response({'hm': season_id, 'hm2': season})
        all_deal_for_season = Deal.objects.filter(created_at__gte=season[season_id][0], created_at__lte=season[season_id][1])
        # return Response({'hm': all_deal_for_season, 'hm2': all_deal_for_season})
        all_quantity_per_season = Deal.objects.aggregate(Sum("quantity"))
        # return Response({'hm': all_deal_for_season, 'hm2': all_quantity_per_season})
        all_name_products_per_season = []
        for deal in all_deal_for_season:
            all_name_products_per_season = deal.id_product__name.distinct()
        # return Response({'hm': all_deal_for_season, 'hm2': all_name_products_per_season})
        all_name_products_and_quantity_per_season = {}
        for name_product in all_name_products_per_season:
            definite_product = all_deal_for_season.filter(id_product__name=name_product)
            for product in definite_product:
                definite_product_quantity = product.quantity
                # if 
        return Response({'hm': all_deal_for_season, 'hm2': all_deal_for_season})
        