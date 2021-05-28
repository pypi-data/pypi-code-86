# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-06 11:48

import balafon.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm', '0020_auto_20180308_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionmenu',
            options={'ordering': ['order_index'], 'verbose_name': 'action men', 'verbose_name_plural': 'action menus'},
        ),
        migrations.AlterField(
            model_name='action',
            name='detail',
            field=models.TextField(blank=True, default='', verbose_name='detail'),
        ),
        migrations.AlterField(
            model_name='action',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='action',
            name='uuid',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='actiondocument',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='actionmenu',
            name='a_attrs',
            field=models.CharField(blank=True, default='', help_text='Example: class="colorbox-form" for colorbos display', max_length=50, verbose_name='Link args'),
        ),
        migrations.AlterField(
            model_name='actionmenu',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='actionstatus',
            name='background_color',
            field=models.CharField(blank=True, default='', help_text='Background color. Must be a rgb code. For example: #000000', max_length=7, validators=[balafon.utils.validate_rgb], verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='actionstatus',
            name='fore_color',
            field=models.CharField(blank=True, default='', help_text='Fore color. Must be a rgb code. For example: #ffffff', max_length=7, validators=[balafon.utils.validate_rgb], verbose_name='Fore color'),
        ),
        migrations.AlterField(
            model_name='actiontype',
            name='action_template',
            field=models.CharField(blank=True, default='', help_text='Action of this type will be displayed using the given template', max_length=200, verbose_name='action template'),
        ),
        migrations.AlterField(
            model_name='actiontype',
            name='default_template',
            field=models.CharField(blank=True, default='', help_text='Action of this type will have a document with the given template', max_length=200, verbose_name='document template'),
        ),
        migrations.AlterField(
            model_name='actiontype',
            name='mail_to_subject',
            field=models.CharField(blank=True, default='', help_text='This would be used as subject when sending the action by email', max_length=100, verbose_name='Subject of email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='billing_street_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='street number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='favorite_language',
            field=models.CharField(blank=True, choices=[('', 'Default'), ('en', 'English'), ('fr', 'Français')], default='', max_length=10, verbose_name='favorite language'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, ''), (1, 'Mr'), (2, 'Mrs'), (3, 'Mrs and Mr')], default=0, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='street number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='uuid',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactsimport',
            name='encoding',
            field=models.CharField(choices=[('utf-8', 'utf-8'), ('iso-8859-15', 'iso-8859-15'), ('cp1252', 'cp1252')], default='utf-8', max_length=50),
        ),
        migrations.AlterField(
            model_name='contactsimport',
            name='separator',
            field=models.CharField(choices=[(',', 'Coma'), (';', 'Semi-colon')], default=',', max_length=5),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='label',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='label'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='widget',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='widget'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='billing_street_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='street number'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='street_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='street number'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='website',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='web site'),
        ),
        migrations.AlterField(
            model_name='group',
            name='background_color',
            field=models.CharField(blank=True, default='', help_text='Background color. Must be a rgb code. For example: #000000', max_length=7, validators=[balafon.utils.validate_rgb], verbose_name='Background color'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='group',
            name='fore_color',
            field=models.CharField(blank=True, default='', help_text='Fore color. Must be a rgb code. For example: #ffffff', max_length=7, validators=[balafon.utils.validate_rgb], verbose_name='Fore color'),
        ),
        migrations.AlterField(
            model_name='mailtosettings',
            name='body_template',
            field=models.TextField(blank=True, default='', verbose_name='body template'),
        ),
        migrations.AlterField(
            model_name='mailtosettings',
            name='subject',
            field=models.CharField(blank=True, default='', help_text='Use action subject if empty', max_length=100, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='detail',
            field=models.TextField(blank=True, default='', verbose_name='detail'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='display_on_board',
            field=models.BooleanField(db_index=True, default=True, verbose_name='display on board'),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='reverse',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='reverse relation'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='code',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='code'),
        ),
    ]
