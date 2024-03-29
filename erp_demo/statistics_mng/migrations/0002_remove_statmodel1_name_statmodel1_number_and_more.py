# Generated by Django 4.2.1 on 2023-07-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_mng', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statmodel1',
            name='name',
        ),
        migrations.AddField(
            model_name='statmodel1',
            name='number',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statmodel1',
            name='operator',
            field=models.CharField(default=1, max_length=99),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='assembly',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='blasting',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='grinding',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='painting',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statmodel1',
            name='welding',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
