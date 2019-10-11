# core django
from django.urls import path
from . import views

urlpatterns = [
    path('live-spot-quotes', views.LiveSpotQuotes.as_view(), name='live_spot_quotes'),
    path('live-future-quotes', views.LiveFutureQuotes.as_view(), name='live_future_quotes')
]
