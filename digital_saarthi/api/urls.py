# core django
from django.urls import path
from django.conf.urls import include
api_version = 'v1'

urlpatterns = [
    path(f'{api_version}/market/', include('market_data.api_urls')),
    path(f'{api_version}/image_recognition/', include('image_recognition.api_urls')),
]
