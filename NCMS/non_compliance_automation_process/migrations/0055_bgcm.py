# Generated by Django 4.2.4 on 2024-10-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_compliance_automation_process', '0054_dcc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BGCM',
            fields=[
                ('bgcm_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('bgcm_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
