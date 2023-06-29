# Generated by Django 4.2.1 on 2023-06-29 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr_mng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessControlPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, unique=True)),
                ('type', models.CharField(choices=[('Prototype', 'Prototype'), ('Pre-launch', 'Pre-launch'), ('Production', 'Production')], max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('revision', models.CharField(max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('team', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='hr_mng.employee')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
