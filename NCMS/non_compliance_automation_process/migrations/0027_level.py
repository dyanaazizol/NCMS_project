# Generated by Django 4.2.4 on 2024-09-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0026_delete_ncreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]