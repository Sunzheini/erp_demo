# Generated by Django 4.1.4 on 2023-04-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_mng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='contact_person',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='correspondence_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='eik',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='mol',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='registration_address',
            field=models.CharField(default=1, max_length=99),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='registration_city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('Person', 'Person'), ('Company', 'Company'), ('Institution', 'Institution')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=99),
        ),
    ]
