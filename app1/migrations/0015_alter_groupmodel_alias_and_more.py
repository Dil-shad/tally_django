# Generated by Django 4.0.5 on 2022-06-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_groupmodel_under'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='alias',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='method_to_allocate_usd_purchase',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]