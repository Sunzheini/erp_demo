# Generated by Django 4.1.4 on 2023-01-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_mng', '0005_process_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='number',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
