# Generated by Django 4.2.1 on 2023-06-12 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newactions_mng', '0001_initial'),
        ('risk_mng', '0003_remove_risk_long_term_action_riskstoactions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='long_term_action',
            field=models.ManyToManyField(blank=True, through='risk_mng.RisksToActions', to='newactions_mng.newaction'),
        ),
        migrations.AlterField(
            model_name='riskstoactions',
            name='action_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newactions_mng.newaction'),
        ),
    ]
