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

        maturity = options['nodetype'][0]
        resources = Resource.objects.all()

        for resource in resources:
            resource.load_tiles()
        # if options['nodetype'][0] not in [str(tile.nodegroup_id) for tile in resource.tiles]:
                # print(resource)
            for tile in resource.tiles:
                if str(tile.nodegroup_id) == options[maturity and tile.data[maturity == 'b1e76238-dd81-4023-995d-a21c4f70cb96' :
                    print(resource)
                    
                    # tile.data = {}
                    # tile.data[options['nodetype'][0]] = 'b1e76238-dd81-4023-995d-a21c4f70cb96'
                    # tile.save()
                    # print(tile.data)
                # newTile = TileModel()
                # newTile.resourceinstance_id = resource.resourceinstanceid
                # newTile.parentTile = None
                # newTile.nodegroup_id = options['nodetype'][0]
                # newTile.sortOrder = 0
                # newTile.provisionaledits = None
                # newTile.data = {options['nodetype'][0]: 'b1e76238-dd81-4023-995d-a21c4f70cb96'}
                # newTile.save()

    #TODO: Write in such way I can understand it !