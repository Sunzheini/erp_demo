# Generated by Django 4.2.1 on 2023-08-04 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_mng', '0004_rename_number_statmodel1_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statmodel1',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='operator',
            field=models.CharField(max_length=99, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
