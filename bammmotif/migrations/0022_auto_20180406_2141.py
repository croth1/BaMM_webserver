# Generated by Django 2.0.3 on 2018-04-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0021_auto_20180406_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestepbammjob',
            name='Motif_Init_File_Format',
            field=models.CharField(choices=[('MEME', 'MEME'), ('BaMM', 'BaMM')], default='MEME', max_length=255),
        ),
    ]
