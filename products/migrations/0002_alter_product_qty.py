# Generated by Django 4.2.8 on 2024-02-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]