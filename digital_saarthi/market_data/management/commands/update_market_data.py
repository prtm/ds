# stdlib
import json

# core django
from django.core.management.base import BaseCommand, CommandError

# third party
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# project related
from digital_saarthi.market_data import helper



class Command(BaseCommand):
    # create an sh file and schedule in CRONTAB or supervisor
    help = 'Update Market Data'

    # Any valid command will call handler
    def handle(self, *args, **options):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('market_data_live_spot_quotes', {
            'type': 'market_data_message',
            'message': json.dumps(helper.get_live_spot_quotes())
        })
        async_to_sync(channel_layer.group_send)('market_data_live_future_quotes', {
            'type': 'market_data_message',
            'message': json.dumps(helper.get_live_future_quotes())
        })