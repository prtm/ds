# core django
from django.urls import path
from django.conf.urls import include
api_version = 'v1'

urlpatterns = [
    path(f'{api_version}/', include('market_data.urls')),
]
