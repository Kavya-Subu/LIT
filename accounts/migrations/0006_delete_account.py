# Generated by Django 4.2.8 on 2024-01-25 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_is_admin_alter_account_is_staff_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]