# Generated by Django 2.1.3 on 2018-11-25 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teamsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 25, 16, 0, 31, 2879, tzinfo=utc)),
        ),
    ]
