from urllib import request
from venv import create
from .models import BadProduct, BestProduct
from product.models import Deal
from datetime import date, timedelta

season = {
    1 : [date(year=date.now()-timedelta(year=2), month=12, day=1), date(year=date.now()-timedelta(year=1), month=2, day=28)],
    2 : [date(year=date.now()-timedelta(year=1), month=3, day=1), date(year=date.now()-timedelta(year=1), month=5, day=31)],
    3 : [date(year=date.now()-timedelta(year=1), month=6, day=1), date(year=date.now()-timedelta(year=1), month=8, day=31)],
    4 : [date(year=date.now()-timedelta(year=1), month=9, day=1), date(year=date.now()-timedelta(year=1), month=11, day=30)],
}

all_deal_for_season = Deal.objects.filter(created_at___gte=season[season_id][0], created_at__lte=season[season_id][1])
