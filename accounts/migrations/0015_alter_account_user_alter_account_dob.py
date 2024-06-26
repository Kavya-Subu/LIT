# Generated by Django 4.2.8 on 2024-02-01 09:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_alter_account_designation_alter_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 9, 24, 40, 533914)),
        ),
    ]
