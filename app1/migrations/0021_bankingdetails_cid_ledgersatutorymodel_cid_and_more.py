# Generated by Django 4.0.5 on 2022-06-16 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_rename_group_id_ledgermodel_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankingdetails',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel'),
        ),
        migrations.AddField(
            model_name='ledgersatutorymodel',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel'),
        ),
        migrations.AddField(
            model_name='mailingaddressmodel',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel'),
        ),
        migrations.AddField(
            model_name='taxregistermodel',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companymodel'),
        ),
    ]
