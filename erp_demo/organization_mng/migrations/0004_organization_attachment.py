# Generated by Django 4.1.4 on 2023-04-20 12:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_mng', '0003_alter_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='attachment',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]
