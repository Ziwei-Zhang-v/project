from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text=_('Latitude of the location of squirrel'),
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text=_('Longitude of the location of squirrel'),
    )

    unique_squirrel_id = models.CharField(
        max_length = 20,
        help_text=_('Unique squirrel id of squirrel'),
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]

    shift = models.CharField(
        max_length=5,
        choices=SHIFT_CHOICES,
        help_text=_('AM or PM'),
    )

    date = models.DateField(
        help_text=_('Date when squirrel observed'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    NONE = ''

    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]   
    
    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        default=NONE,
        help_text=_('Age of squirrel'),
    )


