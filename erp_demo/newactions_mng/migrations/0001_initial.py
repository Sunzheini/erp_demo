# Generated by Django 4.2.1 on 2023-06-12 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr_mng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('target_date', models.DateField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('responsible', models.ForeignKey(db_column='owner_ident', on_delete=django.db.models.deletion.CASCADE, to='hr_mng.employee', to_field='identification')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
