# Generated by Django 4.0.5 on 2022-06-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_groupmodel_method_to_allocate_usd_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='under',
            field=models.CharField(default='primary', max_length=225),
        ),
    ]
