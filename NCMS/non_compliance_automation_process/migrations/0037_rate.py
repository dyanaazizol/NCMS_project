# Generated by Django 4.2.4 on 2024-09-12 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0036_delete_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('actionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='non_compliance_automation_process.action')),
            ],
        ),
    ]