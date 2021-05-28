# Generated by Django 3.1.7 on 2021-05-28 08:04

import django.contrib.postgres.indexes
from django.db import migrations

DROP_OLD_INDEXES = """
DROP INDEX data_france_commune_search_index;
DROP INDEX data_france_elumunicipal_search_index;
"""

RECREATE_OLD_INDEXES = """
CREATE INDEX data_france_commune_search_index ON data_france_commune USING GIN ("search");
CREATE INDEX data_france_elumunicipal_search_index ON data_france_elumunicipal USING GIN ("search");
"""


class Migration(migrations.Migration):

    dependencies = [
        ("data_france", "0021_circonscriptionconsulaire"),
    ]

    operations = [
        migrations.RunSQL(sql=DROP_OLD_INDEXES, reverse_sql=RECREATE_OLD_INDEXES),
        migrations.AddIndex(
            model_name="commune",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search"], name="data_france_search_b703ec_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="elumunicipal",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search"], name="data_france_search_12f115_gin"
            ),
        ),
    ]
