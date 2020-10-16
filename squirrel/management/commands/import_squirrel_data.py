import csv
import datetime

from django.core.management.base import BaseCommand
from squirrel.models import SquirrelDetail



class Command(BaseCommand):
    help = 'Get squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = SquirrelDetail()
                obj.X = item['X']
                obj.Y = item['Y'] 
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.shift = item['Shift']
                obj.date = datetime.strptime(item['Date'], '%m%d%Y').strftime('%Y-%m-%d')
                obj.age = item['Age']
                obj.primary_fur_color = item['Primary Fur Color']
                obj.location = item['Location']
                obj.specific_location = item['Specific Location']
                obj.running = (item['Running'][0] == 't')
                obj.chasing = (item['Chasing'][0] == 't')
                obj.climbing = (item['Climbing'][0] == 't')
                obj.eating = (item['Eating'][0] == 't')
                obj.foraging = (item['Foraging'][0] == 't')
                obj.other_activities = item['Other Activities']
                obj.kuks = (item['Kuks'][0] == 't')
                obj.quaas = (item['Quaas'][0] == 't')
                obj.moans = (item['Moans'][0] == 't')
                obj.tail_flags = (item['Tail flags'][0] == 't')
                obj.tail_twitches = (item['Tail twitches'][0] == 't')
                obj.approaches = (item['Approaches'][0] == 't')
                obj.indifferent = (item['Indifferent'][0] == 't')
                obj.runs_from = (item['Runs from'][0] == 't')
  
                obj.save()
        


        
        msg = f'You are importing from {file_}'
        
         

        self.stdout.write(self.style.SUCCESS(msg))
