# Generated by Django 4.2.1 on 2023-06-29 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_mng', '0002_alter_machine_installation_date_and_more'),
        ('dox_mng', '0013_alter_document_type_alter_documenteditpurgatory_type'),
        ('calibration_mng', '0002_alter_measuringequipment_calibration_interval_in_days_and_more'),
        ('control_plan_mng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessControlPlanStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, unique=True)),
                ('product_characteristics', models.TextField(blank=True, null=True)),
                ('process_characteristics', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('sample_size', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('reaction_plan', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='processcontrolplan',
            name='product',
            field=models.CharField(default=1, max_length=99),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processcontrolplan',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='processcontrolplan',
            name='name',
            field=models.CharField(default='Process Control Plan <built-in function id>', max_length=99, unique=True),
        ),
        migrations.CreateModel(
            name='ProcessControlPlanStepToMeasuringEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measuring_equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_mng.measuringequipment')),
                ('process_control_plan_step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_plan_mng.processcontrolplanstep')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessControlPlanStepToMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_mng.machine')),
                ('process_control_plan_step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_plan_mng.processcontrolplanstep')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessControlPlanStepToDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dox_mng.document')),
                ('process_control_plan_step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_plan_mng.processcontrolplanstep')),
            ],
        ),
        migrations.AddField(
            model_name='processcontrolplanstep',
            name='documents',
            field=models.ManyToManyField(blank=True, through='control_plan_mng.ProcessControlPlanStepToDocuments', to='dox_mng.document'),
        ),
        migrations.AddField(
            model_name='processcontrolplanstep',
            name='machines',
            field=models.ManyToManyField(blank=True, related_name='machines', through='control_plan_mng.ProcessControlPlanStepToMachine', to='maintenance_mng.machine'),
        ),
        migrations.AddField(
            model_name='processcontrolplanstep',
            name='measuring_equipment',
            field=models.ManyToManyField(blank=True, related_name='measuring_equipment', through='control_plan_mng.ProcessControlPlanStepToMeasuringEquipment', to='calibration_mng.measuringequipment'),
        ),
    ]