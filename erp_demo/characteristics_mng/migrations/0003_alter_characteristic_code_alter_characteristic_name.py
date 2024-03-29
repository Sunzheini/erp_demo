# Generated by Django 4.2.1 on 2023-08-04 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics_mng', '0002_characteristic_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristic',
            name='code',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.CharField(max_length=99, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
