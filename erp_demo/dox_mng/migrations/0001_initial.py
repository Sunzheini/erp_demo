# Generated by Django 4.1.4 on 2022-12-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('revision', models.PositiveIntegerField()),
                ('owner', models.CharField(max_length=30)),
                ('attachment', models.FileField(upload_to='')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
