# Generated by Django 2.0.3 on 2018-04-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0030_motifs_m_aurrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bammscanjob',
            name='e_value_cutoff',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='mmcomparejob',
            name='e_value_cutoff',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=3),
        ),
    ]
