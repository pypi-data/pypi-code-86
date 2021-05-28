# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0003_auto_20180409_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_create_group', models.BooleanField(default=True, help_text='If not checked, the user can not create group', verbose_name='can create group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User permissions',
                'verbose_name_plural': 'User permissions',
            },
        ),
    ]
