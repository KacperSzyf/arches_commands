from fileinput import close
from django.core.management.base import BaseCommand, CommandError

#imports
import csv
from arches.app.models.resource import Resource
from arches.app.utils.betterJSONSerializer import JSONSerializer

 
class Command(BaseCommand):
    """
    Description:
    This command a .csv file containing ResourceID and downloads all corresponding resources to jsonl

    Parameters:
    '-s': path to .csv

    Returns:
    '.jsonl': file containing all records
    """
    def add_arguments(self, parser):

        parser.add_argument("-s", "--source", action="store", dest="file_path", default="", help="File path to csv containing ResourceID's")

    def handle(self, *args, **options):
    
        #Load CSV
        resource_ids = []
        csv_path = options['file_path']

        #Open target file as a dictionary
        with open (csv_path, newline="") as csv_file:
            csv_reder = csv.DictReader(csv_file, delimiter=',')
            
            #Copy all ResourceID's to new array
            for row in csv_reder:
                resource_ids.append(row['ResourceID'])


        records = self.get_resource(resource_ids)
        
        self.write_to_file(records)

    def get_resource(self, resource_ids):
        '''
        Description:
        Loads all requested objects from DB 

        Parameters:
        'resource_ids': a list of all requeried ResourceID's

        Returns:
        'records': a list of serialized Resource Objects
        '''
        records = []
        print("in get res")
        for id in resource_ids:
            if Resource.objects.filter(pk=id).exists():
                resource = Resource.objects.get(pk = id)
                resource.load_tiles()
                resource_json = JSONSerializer().serializeToPython(resource)
                records.append(resource_json)

        return records

    def write_to_file(self, records):
        
        with open('json_records.jsonl', 'w') as json_records:
            for record in records:
                print(record)
                json_records.write(str(record) + "\n")
