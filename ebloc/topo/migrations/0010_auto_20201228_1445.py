# Generated by Django 3.1.4 on 2020-12-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topo', '0009_auto_20201226_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='coordinates',
            new_name='geom',
        ),
    ]
