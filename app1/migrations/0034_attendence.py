# Generated by Django 3.2.12 on 2022-07-01 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_unitcreationempwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('attendence_typ', models.CharField(max_length=225)),
                ('cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel')),
            ],
        ),
    ]
