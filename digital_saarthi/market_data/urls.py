# core django
from django.urls import path
from . import views

urlpatterns = [
    path('live-spot-quotes', views.live_spot_quotes,),
    path('live-future-quotes', views.live_future_quotes,)
]
