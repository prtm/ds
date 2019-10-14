# stdlib
import re
import json

# core django

# third party
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# project related
from .helper import get_live_future_quotes, get_live_spot_quotes



class LiveSpotQuotes(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        # TODO: handle error cases
        return Response(get_live_spot_quotes())


class LiveFutureQuotes(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        # TODO: handle error cases
        return Response(get_live_future_quotes())
