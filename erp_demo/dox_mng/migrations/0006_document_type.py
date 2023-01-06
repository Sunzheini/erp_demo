# Generated by Django 4.1.4 on 2023-01-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dox_mng', '0005_alter_document_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(blank=True, choices=[('Manual', 'Manual'), ('Procedure', 'Procedure'), ('Instruction', 'Instruction'), ('Form', 'Form')], max_length=30, null=True),
        ),
    ]
