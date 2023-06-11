# Generated by Django 4.2.1 on 2023-06-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_mng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='ia_test_period',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='immediate_action',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='impact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='risk',
            name='long_term_action',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='new_impact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='new_probability',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='risk',
            name='probability',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]