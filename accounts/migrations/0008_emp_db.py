# Generated by Django 4.2.8 on 2024-01-31 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(default='NA', max_length=50)),
                ('l_name', models.CharField(default='NA', max_length=50)),
                ('phone', models.PositiveIntegerField(default='00', max_length=10)),
                ('address', models.TextField(default='NA', max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'm'), ('Female', 'f'), ('others', 'o')], default=[('Others', 'o')], max_length=10)),
                ('designation', models.CharField(choices=[('Inventory Manager', 'im'), ('Floor Supervisor', 'fs'), ('Staff', 'st')], default='NA', max_length=20)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]