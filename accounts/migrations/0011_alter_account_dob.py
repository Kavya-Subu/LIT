# Generated by Django 4.2.8 on 2024-01-31 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 8, 7, 38, 57729)),
        ),
    ]