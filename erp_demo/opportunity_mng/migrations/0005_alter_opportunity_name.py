# Generated by Django 4.2.1 on 2023-08-04 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity_mng', '0004_opportunitiestoactions_opportunity_long_term_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='name',
            field=models.CharField(max_length=99, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
