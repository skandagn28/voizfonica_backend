# Generated by Django 2.2.4 on 2019-08-11 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0008_auto_20190809_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porting',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 11, 11, 2, 18, 281580)),
        ),
    ]