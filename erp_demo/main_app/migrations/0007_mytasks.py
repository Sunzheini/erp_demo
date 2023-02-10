# Generated by Django 4.1.4 on 2023-02-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_requirements_covered_by_process_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=99)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
