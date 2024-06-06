# Generated by Django 4.2.1 on 2024-02-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance_mng', '0003_alter_machine_name'),
        ('hr_mng', '0005_positions_slug'),
        ('supplier_mng', '0003_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('measurement_unit', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('machines', models.ManyToManyField(blank=True, to='maintenance_mng.machine')),
                ('materials', models.ManyToManyField(blank=True, to='supplier_mng.material')),
                ('work_force', models.ManyToManyField(blank=True, to='hr_mng.positions')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]