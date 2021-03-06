# Generated by Django 3.1.2 on 2020-10-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=13, help_text='Latitude of the sighting of squirrel', max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=13, help_text='Longitude of the sighting of squirrel', max_digits=15)),
                ('unique_squirrel_id', models.CharField(help_text='Unique squirrel id of squirrel', max_length=20)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='AM or PM', max_length=5)),
                ('date', models.DateField(help_text='Date when squirrel observed')),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of squirrel', max_length=10)),
                ('Primary_Fur_Color', models.CharField(blank=True, max_length=50)),
                ('Location', models.CharField(blank=True, max_length=30)),
                ('Specific_Location', models.CharField(blank=True, max_length=30)),
                ('Running', models.BooleanField()),
                ('Chasing', models.BooleanField()),
                ('Climbing', models.BooleanField()),
                ('Eating', models.BooleanField()),
                ('Foraging', models.BooleanField()),
                ('Other_Activities', models.CharField(blank=True, max_length=50)),
                ('Kuks', models.BooleanField()),
                ('Quaas', models.BooleanField()),
                ('Moans', models.BooleanField()),
                ('Tail_flags', models.BooleanField()),
                ('Tail_twitches', models.BooleanField()),
                ('Approaches', models.BooleanField()),
                ('Indifferent', models.BooleanField()),
                ('Runs_from', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Squirrel',
        ),
    ]
