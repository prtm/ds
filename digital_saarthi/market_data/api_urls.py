# core django
from django.urls import path
from . import api

urlpatterns = [
    path('live-spot-quotes', api.LiveSpotQuotes.as_view(), name='live_spot_quotes'),
    path('live-future-quotes', api.LiveFutureQuotes.as_view(), name='live_future_quotes')
]
