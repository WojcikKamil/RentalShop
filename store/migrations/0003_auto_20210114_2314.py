# Generated by Django 3.1.5 on 2021-01-14 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210114_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 23, 14, 10, 825700)),
        ),
    ]
