# Generated by Django 3.1.4 on 2021-01-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topo', '0010_auto_20201228_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='annee',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='line',
            name='avis_1',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='line',
            name='avis_2',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='line',
            name='da_nom',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='line',
            name='ext',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='line',
            name='first_ascent',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='line',
            name='obs_cat',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='line',
            name='obs_en',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='line',
            name='obs_es',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='line',
            name='obs_fr',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='line',
            name='ouvert',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='line',
            name='var',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
