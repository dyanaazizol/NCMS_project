# Generated by Django 4.2.4 on 2024-09-02 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doer',
            fields=[
                ('doer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('direct_supervisor', models.CharField(max_length=100)),
                ('gm_hod', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('subsidiary', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('vertical', models.CharField(max_length=50)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.division')),
            ],
        ),
    ]
