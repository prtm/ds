# stdlib
import json

# core django
from django.shortcuts import render
from django.utils.safestring import mark_safe

# project related
from .helper import get_live_future_quotes, get_live_spot_quotes


def live_spot_quotes(request):
    room_name = 'live_spot_quotes'
    return render(request, 'market_data/index.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'initial_data': get_live_spot_quotes(),
    })


def live_future_quotes(request):
    room_name = 'live_future_quotes'
    return render(request, 'market_data/index.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'initial_data': get_live_future_quotes(),
    })
