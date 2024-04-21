from os import name
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema
from django.db.models import Sum
from .models import BadProduct, BestProduct
from product.models import Deal
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from .serializers import BestProductModelSerializer, YourRequestSerializerModelSerializer, BadProductModelSerializer
from rest_framework.response import Response
import operator
from product.models import Product


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
    serializer_for_best = BestProductModelSerializer
    serializer_for_bad = BadProductModelSerializer

    def post(self, request):
        season_id = request.data['season_id']
        all_deal_for_season = Deal.objects.filter(created_at__gte=season[season_id][0], created_at__lte=season[season_id][1])
        all_quantity_per_season = Deal.objects.aggregate(Sum("quantity"))
        all_name_products_per_season = []
        
        for deal in all_deal_for_season:
            all_name_products_per_season = deal.id_product.name
        all_name_products_per_season.distinct()
        all_name_products_and_quantity_per_season = {}
        return Response({'hr': all_name_products_per_season})
        for name_product in all_name_products_per_season:
            definite_product = all_deal_for_season.filter(id_product__name=name_product)
            return Response({'hr': definite_product})
            for product in definite_product:
                definite_product_quantity = product.product_quantity
                
                if name_product in all_name_products_and_quantity_per_season:
                    all_name_products_and_quantity_per_season[product] += definite_product_quantity.product_quantity
                all_name_products_and_quantity_per_season[name_product] = definite_product_quantity.product_quantity
        # return Response({'hr': all_name_products_and_quantity_per_season})
        best_product = BestProduct.objects.create(max(all_name_products_and_quantity_per_season, key=all_name_products_and_quantity_per_season.get))
        bad_product = BadProduct.objects.create(min(all_name_products_and_quantity_per_season, key=all_name_products_and_quantity_per_season.get))
        serializer_bad = self.serializer_for_bad(bad_product)
        serializer_best = self.serializer_for_best(best_product)
        if serializer_bad.is_valid() and serializer_best.is_valid():
            return Response(serializer_bad.validated_data, serializer_best.validated_data)
