# Generated by Django 4.2.4 on 2024-09-12 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0027_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('action_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('action_details', models.TextField(max_length=300)),
                ('levelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.level')),
            ],
        ),
    ]
