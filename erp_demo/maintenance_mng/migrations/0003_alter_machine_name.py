# Generated by Django 4.2.1 on 2023-08-04 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_mng', '0002_alter_machine_installation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=99, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
