# Generated by Django 3.1.7 on 2021-04-03 19:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_auto_20210404_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 19, 1, 37, 247692, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='EventsRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.event')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='APP.student')),
            ],
        ),
    ]
