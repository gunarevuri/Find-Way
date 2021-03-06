# Generated by Django 3.0.1 on 2020-06-17 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0005_auto_20200617_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busstation',
            old_name='lati',
            new_name='latitud',
        ),
        migrations.RenameField(
            model_name='busstation',
            old_name='longi',
            new_name='longitud',
        ),
        migrations.AlterField(
            model_name='timings',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 17, 13, 52, 20, 37898, tzinfo=utc)),
        ),
    ]
