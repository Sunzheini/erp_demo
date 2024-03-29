# Generated by Django 4.2.1 on 2023-07-21 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mng', '0003_alter_employee_position_and_more'),
        ('process_mng', '0004_alter_process_process_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='responsible',
            field=models.ForeignKey(db_column='responsible_ident', null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr_mng.employee', to_field='identification'),
        ),
    ]
