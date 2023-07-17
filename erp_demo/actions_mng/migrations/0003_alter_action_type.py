# Generated by Django 4.2.1 on 2023-06-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions_mng', '0002_action_content_type_action_object_id_action_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='type',
            field=models.CharField(choices=[('Containment', 'Containment'), ('Correction', 'Correction'), ('Corrective Action', 'Corrective Action'), ('Systematic Action', 'Systematic Action'), ('Improvement', 'Improvement'), ('Task', 'Task')], max_length=50),
        ),
    ]