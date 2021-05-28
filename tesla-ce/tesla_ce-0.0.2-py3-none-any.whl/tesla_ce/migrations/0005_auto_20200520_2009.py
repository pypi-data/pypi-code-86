# Generated by Django 3.0.6 on 2020-05-20 18:09

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('tesla_ce', '0004_launcher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmentsession',
            name='connector',
        ),
        migrations.CreateModel(
            name='AssessmentSessionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connector', models.FileField(help_text='Connector JS file for this session', upload_to='')),
                ('data', models.FileField(help_text='Data for this session', upload_to='')),
                ('session', models.ForeignKey(help_text='Related assessment session', on_delete=django.db.models.deletion.CASCADE, to='tesla_ce.AssessmentSession')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
