# Generated by Django 4.0.5 on 2022-06-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_stockgroupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scat_name', models.CharField(max_length=225)),
                ('scat_alias', models.CharField(max_length=225)),
                ('scat_under', models.CharField(max_length=225)),
            ],
        ),
    ]