# Generated by Django 4.1.4 on 2023-04-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_mng', '0007_alter_customer_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='attachment',
        ),
    ]