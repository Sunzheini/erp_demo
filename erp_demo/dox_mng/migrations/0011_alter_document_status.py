# Generated by Django 4.1.4 on 2023-05-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dox_mng', '0010_alter_documentlikestousers_document_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('Latest rev', 'Latest rev'), ('Under rev', 'Under rev')], max_length=30),
        ),
    ]