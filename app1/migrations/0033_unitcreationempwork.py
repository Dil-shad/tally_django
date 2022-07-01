# Generated by Django 4.0.5 on 2022-07-01 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_employeegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitCreationEmpWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=225)),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('quc', models.CharField(max_length=225)),
                ('num_decimal_plce', models.CharField(max_length=225)),
                ('cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel')),
            ],
        ),
    ]
