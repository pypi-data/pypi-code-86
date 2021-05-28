# Generated by Django 2.2.10 on 2020-02-18 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bridger", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID",),),
                ("title", models.CharField(max_length=512)),
                ("message", models.TextField(blank=True, null=True)),
                ("buttons", models.JSONField(blank=True, default=dict, null=True),),
                ("timestamp_created", models.DateTimeField(auto_now_add=True)),
                ("timestamp_received", models.DateTimeField(blank=True, null=True)),
                ("timestamp_read", models.DateTimeField(blank=True, null=True)),
                ("timestamp_mailed", models.DateTimeField(blank=True, null=True)),
                (
                    "send_type",
                    models.CharField(
                        choices=[("system", "System"), ("mail", "Mail"), ("system_and_mail", "System and Mail"),],
                        default="system",
                        max_length=32,
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="notifications", to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
