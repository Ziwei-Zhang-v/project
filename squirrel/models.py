from django.db import models
from django.forms import ModelForm
from django.urls import reverse

class Meta:
    managed = True
    
class SquirrelDetail(models.Model):
    X = models.FloatField(
        help_text='Longitude of the sighting of squirrel',
        )

    Y = models.FloatField(
        help_text='Latitude of the sighting of squirrel',
        )

    unique_squirrel_id = models.CharField(
        max_length = 50,
        help_text='Unique Squirrel ID',
        primary_key= True,
        default = None,
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
        null = True,
        help_text=('Age of squirrel'),
    )

    primary_fur_color = models.CharField(max_length=50, null=True)

    location = models.CharField(max_length=30, null=True)

    specific_location = models.CharField(max_length=30, null=True)

    TRUE='TRUE'
    FALSE='FALSE'
    CHOICES=(
            (TRUE,'TRUE'),
            (FALSE,'FALSE'),
            )
    
    running = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Running'))
    
    chasing = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Chasing'))
    
    climbing = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Climbing'))
    
    eating = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Eating'))
    foraging = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Foraging'))
    
    other_activities = models.CharField(
            max_length=100,
            help_text=('Other Activities'),
            null = True)
    
    kuks = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Kuks'))

    quaas = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Quaas'))
    
    moans = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Moans'))
    
    tail_flags = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Tail flags'))
    
    tail_twitches = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Tail twitches'))
    
    approaches = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Approaches'))
    
    indifferent = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Indifferent'))
    
    runs_from = models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=('Runs_from'))


    def __str__(self):
        return self.unique_squirrel_id
    def get_absolute_url(self):
        return reverse('squirrels-detail', kwargs={'id':self.Unique_squirrel_id})

