from django.db import models

    
class SquirrelDetail(models.Model):
    latitude = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        help_text='Latitude of the sighting of squirrel',
    )

    longitude = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        help_text='Longitude of the sighting of squirrel',
    )

    unique_squirrel_id = models.CharField(
        max_length = 20,
        help_text='Unique squirrel id of squirrel',
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    shift = models.CharField(
        max_length=5,
        choices=SHIFT_CHOICES,
        help_text='AM or PM',
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

    primary_fur_color = models.CharField(max_length=50, blank=True)

    location = models.CharField(max_length=30, blank=True)

    specific_location = models.CharField(max_length=30, blank=True)

    running = models.BooleanField()
    
    chasing = models.BooleanField()
    
    climbing = models.BooleanField()
    
    eating = models.BooleanField()
    
    foraging = models.BooleanField()
    
    other_activities = models.CharField(max_length=50, blank=True)
    
    kuks = models.BooleanField()
    
    quaas = models.BooleanField()
    
    moans = models.BooleanField()
    
    tail_flags = models.BooleanField()
    
    tail_twitches = models.BooleanField()
    
    approaches = models.BooleanField()
    
    indifferent = models.BooleanField()
    
    runs_from = models.BooleanField()
