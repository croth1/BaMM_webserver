# Generated by Django 2.0.3 on 2018-05-03 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0040_auto_20180503_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bammjob',
            name='bgModel_File',
        ),
    ]