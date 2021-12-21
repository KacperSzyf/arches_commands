from django.core.management.base import BaseCommand, CommandError

from arches.app.utils.betterJSONSerializer import JSONSerializer
from arches.app.models.resource import Resource
from arches.app.models.models import TileModel

import json

class Command(BaseCommand):
    '''
    Decription:
    Print all specific nodegroup tiles in styled json
    '''
    def add_arguments(self, parser):
        parser.add_argument('nodetype', nargs='+', type=str)

    def handle(self, *args, **options):

        tiles = TileModel.objects.filter(nodegroup_id = options['nodetype'][0])

        for tile in tiles:
            if not tile.data:
                print(tile.data)


        
