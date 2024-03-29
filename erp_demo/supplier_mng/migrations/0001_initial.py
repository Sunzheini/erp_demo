# Generated by Django 4.2.1 on 2023-06-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nonconformity_mng', '0005_remove_nonconformity_systematic_actions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SuppliersToClaims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonconformity_mng.nonconformity')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier_mng.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='claims',
            field=models.ManyToManyField(blank=True, through='supplier_mng.SuppliersToClaims', to='nonconformity_mng.nonconformity'),
        ),
    ]
