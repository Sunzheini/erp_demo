# Generated by Django 4.2.1 on 2023-06-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(choices=[('Product', 'Product'), ('Process', 'Process')], max_length=50)),
                ('requirement', models.CharField(blank=True, max_length=199, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
