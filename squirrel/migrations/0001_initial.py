# Generated by Django 3.1.2 on 2020-10-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, help_text='Latitude of the location of squirrel', max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, help_text='Longitude of the location of squirrel', max_digits=9)),
                ('unique_squirrel_id', models.CharField(help_text='Unique squirrel id of squirrel', max_length=20)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='AM or PM', max_length=5)),
                ('date', models.DateField(help_text='Date when squirrel observed')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='', help_text='Age of squirrel', max_length=10)),
            ],
        ),
    ]
