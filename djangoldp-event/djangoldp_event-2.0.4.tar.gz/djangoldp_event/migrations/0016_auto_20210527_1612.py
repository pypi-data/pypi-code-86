# Generated by Django 2.2.23 on 2021-05-27 14:12

from django.db import migrations, models
import django.db.models.deletion
import djangoldp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangoldp_event', '0015_event_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regionevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlid', djangoldp.fields.LDPUrlField(blank=True, null=True, unique=True)),
                ('is_backlink', models.BooleanField(default=False, help_text='set automatically to indicate the Model is a backlink')),
                ('allow_create_backlink', models.BooleanField(default=True, help_text='set to False to disable backlink creation after Model save')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Région')),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view', 'control'],
                'depth': 0,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoldp_event.Regionevent', verbose_name='Région'),
        ),
    ]
