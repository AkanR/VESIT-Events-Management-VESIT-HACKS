# Generated by Django 3.1.7 on 2021-04-03 21:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_auto_20210404_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 21, 6, 36, 408911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_head',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='soc_head',
            field=models.CharField(blank=True, choices=[('CSI_HEAD', 'CSI_HEAD'), ('IEEE_HEAD', 'IEEE_HEAD'), ('ISA_HEAD', 'ISA_HEAD'), ('ISTE_HEAD', 'ISTE_HEAD'), ('VESLIT_HEAD', 'VESLIT_HEAD'), ('ECELL_HEAD', 'ECELL_HEAD'), ('PHOTOCIRCLE_HEAD', 'PHOTOCIRCLE_HEAD'), ('SORT_HEAD', 'SORT_HEAD'), ('MUSIC_HEAD', 'MUSIC_HEAD'), ('SPORTS_HEAD', 'SPORTS_HEAD'), ('CULTURAL_HEAD', 'CULTURAL_HEAD')], default='', max_length=30),
        ),
    ]
