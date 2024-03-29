# Generated by Django 4.2.1 on 2023-07-20 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mng', '0003_alter_employee_position_and_more'),
        ('newactions_mng', '0002_alter_newaction_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newaction',
            name='responsible',
            field=models.ForeignKey(db_column='owner_ident', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible', to='hr_mng.employee', to_field='identification'),
        ),
    ]
