# Generated by Django 3.1.2 on 2020-10-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0003_auto_20201015_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirreldetail',
            name='unique_squirrel_id',
            field=models.CharField(help_text='Unique squirrel id of squirrel', max_length=14),
        ),
    ]
