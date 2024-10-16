# Generated by Django 4.2.4 on 2024-10-09 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0053_doer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCC',
            fields=[
                ('dcc_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('dcc_email', models.EmailField(max_length=254)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.division')),
            ],
        ),
    ]