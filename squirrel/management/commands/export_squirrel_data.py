import csv

from django.core.management.base import BaseCommand, CommandError
from squirrel.models import SquirrelDetail

class Command(BaseCommand):
    help = 'Export the squirrel data as csv'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')

    def handle(self,*args,**kwargs):
        path = args[0]
        fields = SquirrelDetail._meta.fields
        with open(path,'w') as f:
            writer = csv.writer(f)
            for obj in SquirrelDetail.objects.all():
                row = [getattr(obj,field.name) for field in fields]
                writer.writerow(row)
            f.close()          

