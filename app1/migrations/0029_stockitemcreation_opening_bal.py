# Generated by Django 4.0.5 on 2022-06-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_alter_stockitemcreation_sunder'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemcreation',
            name='opening_bal',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
