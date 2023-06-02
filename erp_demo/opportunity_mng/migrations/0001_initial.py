# Generated by Django 4.2.1 on 2023-06-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
