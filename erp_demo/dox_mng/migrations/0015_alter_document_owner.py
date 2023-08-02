# Generated by Django 4.2.1 on 2023-07-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mng', '0002_alter_accesslevels_description_and_more'),
        ('dox_mng', '0014_alter_document_name_alter_document_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(db_column='owner_ident', null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr_mng.employee', to_field='identification'),
        ),
    ]