# Generated by Django 4.1.4 on 2023-01-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='starting_date',
            field=models.DateField(),
        ),
    ]