# Generated by Django 4.1.4 on 2023-04-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_mng', '0002_customer_contact_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact_person',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='correspondence_address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(),
        ),
    ]
