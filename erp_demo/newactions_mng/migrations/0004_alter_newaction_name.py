# Generated by Django 4.2.1 on 2023-08-04 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newactions_mng', '0003_alter_newaction_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newaction',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
