# Generated by Django 2.0 on 2019-08-09 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0003_auto_20190809_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porting',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 9, 11, 22, 56, 697349)),
        ),
    ]
