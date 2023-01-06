# Generated by Django 4.1.4 on 2023-01-06 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dox_mng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Managerial', 'Managerial'), ('Operational', 'Procedure'), ('Support', 'Support')], max_length=30)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Terminator', 'Terminator'), ('Process', 'Process'), ('Decision', 'Decision')], max_length=30)),
                ('name', models.CharField(max_length=31, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProcessStepToDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dox_mng.document')),
                ('process_step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_mng.processstep')),
            ],
        ),
        migrations.AddField(
            model_name='processstep',
            name='documents',
            field=models.ManyToManyField(through='process_mng.ProcessStepToDocuments', to='dox_mng.document'),
        ),
        migrations.AddField(
            model_name='processstep',
            name='parent_process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_mng.process'),
        ),
    ]
