# Generated by Django 4.2.8 on 2024-01-31 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_account_address_account_designation_account_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 8, 3, 34, 268694)),
        ),
    ]
