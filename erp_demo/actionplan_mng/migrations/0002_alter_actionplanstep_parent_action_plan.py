# Generated by Django 4.2.1 on 2023-06-15 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actionplan_mng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplanstep',
            name='parent_action_plan',
            field=models.ForeignKey(db_column='parent_action_plan_id', on_delete=django.db.models.deletion.CASCADE, to='actionplan_mng.actionplan'),
        ),
    ]