# Generated by Django 2.2.4 on 2019-08-12 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0022_auto_20190811_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porting',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 12, 5, 5, 56, 505606)),
        ),
    ]