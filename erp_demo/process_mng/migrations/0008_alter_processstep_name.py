# Generated by Django 4.1.4 on 2023-01-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_mng', '0007_processstep_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]