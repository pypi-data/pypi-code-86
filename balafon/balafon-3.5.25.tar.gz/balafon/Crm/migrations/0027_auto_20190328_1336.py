# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0026_auto_20180924_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='favorite_language',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='favorite language'),
        ),
    ]
