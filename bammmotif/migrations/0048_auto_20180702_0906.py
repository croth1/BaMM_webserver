# Generated by Django 2.0.6 on 2018-07-02 09:06

import bammmotif.mmcompare.models
import bammmotif.utils.misc
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bammmotif', '0047_auto_20180513_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bammjob',
            name='Background_Sequences',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/media/'), upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammjob',
            name='Input_Sequences',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/media/'), upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammjob',
            name='Motif_InitFile',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/media/'), upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammscanjob',
            name='Background_Sequences',
            field=models.FileField(blank=True, null=True, upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammscanjob',
            name='Input_Sequences',
            field=models.FileField(null=True, upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammscanjob',
            name='Motif_InitFile',
            field=models.FileField(blank=True, null=True, upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='bammscanjob',
            name='bgModel_File',
            field=models.FileField(blank=True, null=True, upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='mmcomparejob',
            name='Motif_InitFile',
            field=models.FileField(null=True, upload_to=bammmotif.mmcompare.models.job_directory_path_motif, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='mmcomparejob',
            name='bgModel_File',
            field=models.FileField(blank=True, null=True, upload_to=bammmotif.mmcompare.models.job_directory_path_motif, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='pengjob',
            name='bg_sequences',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/media/'), upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
        migrations.AlterField(
            model_name='pengjob',
            name='fasta_file',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/media/'), upload_to=bammmotif.utils.misc.job_upload_to_input, validators=[bammmotif.utils.misc.file_size_validator]),
        ),
    ]
