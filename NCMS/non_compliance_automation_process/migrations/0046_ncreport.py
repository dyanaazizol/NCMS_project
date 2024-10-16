# Generated by Django 4.2.4 on 2024-10-09 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0045_delete_ncreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(default='Policy', max_length=255)),
                ('process_owner', models.CharField(default='Process Owner', max_length=255)),
                ('dateIncident', models.DateField()),
                ('typeRef', models.TextField()),
                ('refNo', models.TextField()),
                ('conProjectName', models.TextField()),
                ('accName', models.TextField()),
                ('poDivision', models.TextField()),
                ('scenarioDetails', models.TextField()),
                ('catJus', models.TextField()),
                ('poFI', models.TextField()),
                ('nonFI', models.TextField()),
                ('frequency', models.TextField()),
                ('level', models.CharField(default='pending..', max_length=255)),
                ('doerJustification', models.TextField(default='pending..')),
                ('remarksBGCM', models.TextField(default='pending..')),
                ('remarksHCBD', models.TextField(default='pending..')),
                ('clarificationDate', models.TextField(default='pending..')),
                ('ncDecision', models.TextField(default='pending..')),
                ('remarksPO', models.TextField(default='pending..')),
                ('action', models.TextField(default='pending..')),
                ('acknowledgment', models.TextField(default='pending..')),
                ('status', models.TextField(default='pending..')),
                ('dccID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.dcc')),
                ('doerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.doer')),
                ('rateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.rate')),
                ('scenarioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.scenario')),
            ],
        ),
    ]
