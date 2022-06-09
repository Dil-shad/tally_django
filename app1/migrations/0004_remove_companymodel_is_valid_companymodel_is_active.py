# Generated by Django 4.0.5 on 2022-06-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_companymodel_is_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companymodel',
            name='is_valid',
        ),
        migrations.AddField(
            model_name='companymodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
