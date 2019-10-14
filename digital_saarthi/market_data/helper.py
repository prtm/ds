# stdlib
import re
import json


# third party
import html5lib
from bs4 import BeautifulSoup
import requests


def get_live_spot_quotes():
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
    return table_data


def get_live_future_quotes():
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
    return table_data
