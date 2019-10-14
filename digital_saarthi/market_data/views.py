# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def live_spot_quotes(request):
    room_name = 'live_spot_quotes'
    return render(request, 'market_data/index.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def live_future_quotes(request):
    room_name = 'live_future_quotes'
    return render(request, 'market_data/index.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })