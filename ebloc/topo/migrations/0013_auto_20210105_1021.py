# Generated by Django 3.1.4 on 2021-01-05 10:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topo', '0012_auto_20210105_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.RenameField(
            model_name='topo',
            old_name='location',
            new_name='geom',
        ),
    ]
