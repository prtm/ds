# stdlib
import re
import json

# core django
from django.contrib.auth.models import User

# third party
import html5lib
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import requests


class LiveSpotQuotes(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        url = requests.get(
            'http://ncdex.com/MarketData/LiveSpotQuotes.aspx', verify=False)
        soup = BeautifulSoup(url.content.decode('utf-8'), "html5lib")
        cells = soup.find_all('td', width='120', text=re.compile(r'\s+Maize'))
        headings = [row.text.strip() for row in soup.find(
            'tr', {'class': 'HeaderColor'}).find_all('th')]
        table_data = []
        for cell in cells:
            row = {}
            parent = cell.parent('td')
            for i in range(len(cell.parent('td'))):
                row[headings[i]] = parent[i].text.strip()
            table_data.append(row)
        return Response(table_data)


class LiveFutureQuotes(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        url = requests.get(
            'https://ncdex.com/MarketData/LiveFuturesQuotes.aspx', verify=False)
        soup = BeautifulSoup(url.content.decode('utf-8'), "html5lib")
        cell = soup.find('a', text=re.compile(r'\s+Maize'))
        parent = cell.parent.parent('td')
        headings = []
        for row in soup.find_all('th', scope="col"):
            val = row.get_text().strip()
            if val:
                headings.append(val)
        table_data = {}
        for i in range(len(cell.parent.parent('td'))-1):
            table_data[headings[i]] = parent[i].text.strip()
        return Response(table_data)
