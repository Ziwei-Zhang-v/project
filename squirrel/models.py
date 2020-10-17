from django.db import models
from django.forms import ModelForm
from django.urls import reverse

class Meta:
    managed=True
    
class SquirrelDetail(models.Model):
    X = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        help_text='Longitude of the sighting of squirrel',
        )

    Y = models.DecimalField(
        max_digits=15,
        decimal_places=13,
        help_text='Latitude of the sighting of squirrel',
        )

    unique_squirrel_id = models.CharField(
        max_length =50,
        help_text='Unique Squirrel ID',
        primary_key=True,
        default=None,
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

    AGE_CHOICES = [
        (ADULT, ('Adult')),
        (JUVENILE, ('Juvenile')),
    ]   
    
    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        null=True,
        help_text=('Age of squirrel'),
    )

    primary_fur_color = models.CharField(
        max_length=50, 
        null=True
    )

    location = models.CharField(
        max_length=30,
        null=True,
    )

    specific_location = models.CharField(
        max_length=30, 
        null=True,
    )
    
    running = models.BooleanField(
            help_text=('Is the squirrel running?'),
    )
    
    chasing = models.BooleanField(
            help_text=('Is the squirrel chasing?'),
    )
    
    climbing = models.BooleanField(
            help_text=('Is the squirrel climbing?'),
    )   

    eating = models.BooleanField(
            help_text=('Is the squirrel eating?'),
    )  

    foraging = models.BooleanField(
            help_text=('Is the squirrel foraging?'),
    )  

    other_activities = models.CharField(
            max_length=100,
            help_text=('Other Activities'),
            null=True)
    
    kuks = models.BooleanField(
            help_text=('The squirrel kuks?'),
    )  

    quaas = models.BooleanField(
            help_text=('The squirrel quaas?'),
    )  

    moans = models.BooleanField(
            help_text=('The squirrel moans?'),
    )  

    tail_flags = models.BooleanField(
            help_text=('Tail flags'),
    )
    
    tail_twitches = models.BooleanField(
            help_text=('Tail twitches'),
    )
    
    approaches = models.BooleanField(
            help_text=('Approaches'),
    )
    
    indifferent = models.BooleanField(
            help_text=('Indifferent'),
    )
    
    runs_from = models.BooleanField(
            help_text=('Runs_from'),
    )


    def __str__(self):
        return self.unique_squirrel_id

    def get_absolute_url(self):
        return reverse('squirrels-detail', kwargs={'id':self.Unique_squirrel_id})


