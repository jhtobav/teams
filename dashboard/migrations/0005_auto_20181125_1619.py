# Generated by Django 2.1.3 on 2018-11-25 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20181125_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 25, 16, 19, 4, 638766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 25, 16, 19, 4, 639844, tzinfo=utc)),
        ),
    ]
