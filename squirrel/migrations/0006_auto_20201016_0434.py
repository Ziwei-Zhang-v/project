# Generated by Django 3.1.2 on 2020-10-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0005_auto_20201016_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirreldetail',
            old_name='longitude',
            new_name='X',
        ),
        migrations.RenameField(
            model_name='squirreldetail',
            old_name='latitude',
            new_name='Y',
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of squirrel', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='approaches',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Approaches', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='chasing',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Chasing', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='climbing',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Climbing', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='eating',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Eating', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='foraging',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Foraging', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='indifferent',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Indifferent', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='kuks',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Kuks', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='moans',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Moans', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='other_activities',
            field=models.CharField(help_text='Other Activities', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='primary_fur_color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='quaas',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Quaas', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='running',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Running', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='runs_from',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Runs_from', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='specific_location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='tail_flags',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Tail flags', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='tail_twitches',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Tail twitches', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirreldetail',
            name='unique_squirrel_id',
            field=models.CharField(default=None, help_text='Unique Squirrel ID', max_length=50, primary_key=True, serialize=False),
        ),
    ]
