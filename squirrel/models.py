from django.db import models

    
class SquirrelDetail(models.Model):
    latitude = models.DecimalField(
        max_digits = 15,
        decimal_places = 13,
        help_text=('Latitude of the location of squirrel'),
    )

    longitude = models.DecimalField(
        max_digits= 15,
        decimal_places = 13,
        help_text=('Longitude of the location of squirrel'),
    )

    unique_squirrel_id = models.CharField(
        max_length = 20,
        help_text=('Unique squirrel id of squirrel'),
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, ('AM')),
        (PM, ('PM')),
    ]

    shift = models.CharField(
        max_length=5,
        choices=SHIFT_CHOICES,
        help_text=('AM or PM'),
    )

    date = models.DateField(
        help_text=('Date when squirrel observed'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    NONE = ''

    AGE_CHOICES = [
        (ADULT, ('Adult')),
        (JUVENILE, ('Juvenile')),
    ]   
    
    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        blank = True,
        help_text=('Age of squirrel'),
    )

    Primary_Fur_Color = models.CharField(max_length=50, blank = True)

    Location = models.CharField(max_length=30, blank = True)

    Specific_Location = models.CharField(max_length=30, blank = True)

    Running = models.BooleanField()
    
    Chasing = models.BooleanField()
    
    Climbing = models.BooleanField()
    
    Eating = models.BooleanField()
    
    Foraging = models.BooleanField()
    
    Other_Activities = models.CharField(max_length=50, blank = True)
    
    Kuks = models.BooleanField()
    
    Quaas = models.BooleanField()
    
    Moans = models.BooleanField()
    
    Tail_flags = models.BooleanField()
    
    Tail_twitches = models.BooleanField()
    
    Approaches = models.BooleanField()
    
    Indifferent = models.BooleanField()
    
    Runs_from = models.BooleanField()


