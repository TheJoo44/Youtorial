# Generated by Django 3.0.2 on 2020-03-23 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='saved',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 10, 25, 52, 115770), verbose_name='date saved'),
        ),
    ]
