# Generated by Django 2.0.3 on 2018-05-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0038_auto_20180421_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bammjob',
            name='score_Cutoff',
            field=models.FloatField(default=0.0001),
        ),
        migrations.AlterField(
            model_name='bammscanjob',
            name='score_Cutoff',
            field=models.FloatField(default=0.0001),
        ),
        migrations.AlterField(
            model_name='onestepbammjob',
            name='score_Cutoff',
            field=models.FloatField(default=0.0001),
        ),
    ]
