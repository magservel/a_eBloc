# Generated by Django 3.1.4 on 2020-12-26 09:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topo', '0006_remove_topo_geom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('coordinates', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('photo', models.ImageField(upload_to='points/.')),
                ('bloc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topo.bloc')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='lines/.')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topo.point')),
            ],
        ),
        migrations.AddField(
            model_name='bloc',
            name='sector',
            field=models.ForeignKey(on_delete=models.SET(0), to='topo.sector'),
        ),
    ]
