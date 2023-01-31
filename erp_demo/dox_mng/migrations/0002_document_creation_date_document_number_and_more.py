# Generated by Django 4.1.4 on 2023-01-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dox_mng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='creation_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='revision_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='revision_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
