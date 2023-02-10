# Generated by Django 4.1.4 on 2023-02-10 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mng', '0001_initial'),
        ('process_mng', '0002_alter_processstep_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='process_owner',
            field=models.ForeignKey(db_column='responsible_ident', default=1, on_delete=django.db.models.deletion.CASCADE, to='hr_mng.employee', to_field='identification'),
            preserve_default=False,
        ),
    ]
