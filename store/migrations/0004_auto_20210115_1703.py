# Generated by Django 3.1.5 on 2021-01-15 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210114_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 15, 17, 3, 52, 672597)),
        ),
    ]