# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/market-data/(?P<room_name>\w+)/$', consumers.MarketDataConsumer),
]