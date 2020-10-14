import csv

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
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Hectare = item['Hectare']

                
                obj.Date = item['Date']
                obj.Hectare_Squirrel_Number = item['Hectare Squirrel Number']
                obj.Age = item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Highlight_Fur_Color = item['Highlight Fur Color']
                obj.Combination_of_Primary_and_Highlight_Color = item['Combination of Primary and Highlight Color']
                obj.Color_notes = item['Color notes']
                obj.Location = item['Location']
                obj.Above_Ground_Sighter_Measurement = item['Above Ground Sighter Measurement']
                obj.Specific_Location = item['Specific Location']
                
                obj.Running = bool(item['Running'])
                obj.Chasing = bool(item['Chasing'])
                obj.Climbing = bool(item['Climbing'])
                obj.Eating = bool(item['Eating'])
                obj.Foraging = bool(item['Foraging'])
                obj.Other_Activities = item['Other Activities']
                obj.Kuks = bool(item['Kuks'])
                obj.Quaas = bool(item['Quaas'])
                obj.Moans = bool(item['Moans'])
                obj.Tail_flags = bool(item['Tail flags'])
                obj.Tail_twitches = bool(item['Tail twitches'])
                obj.Approaches = bool(item['Approaches'])
                obj.Indifferent = bool(item['Indifferent'])
                obj.Runs_from = bool(item['Runs from'])
                obj.Other_Interactions = item['Other Interactions']
                obj.Lat_Long = item['Lat/Long']
  
                obj.save()
        


        
        msg = f'You are importing from {file_}'
        
         

        self.stdout.write(self.style.SUCCESS(msg))
