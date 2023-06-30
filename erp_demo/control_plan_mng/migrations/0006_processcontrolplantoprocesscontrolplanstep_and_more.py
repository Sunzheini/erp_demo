# Generated by Django 4.2.1 on 2023-06-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_plan_mng', '0005_remove_processcontrolplanstep_characteristics_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessControlPlanToProcessControlPlanStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_control_plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_plan_mng.processcontrolplan')),
                ('process_control_plan_step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_plan_mng.processcontrolplanstep')),
            ],
        ),
        migrations.AddField(
            model_name='processcontrolplan',
            name='steps',
            field=models.ManyToManyField(blank=True, through='control_plan_mng.ProcessControlPlanToProcessControlPlanStep', to='control_plan_mng.processcontrolplanstep'),
        ),
    ]
