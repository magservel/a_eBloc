# Generated by Django 3.1.4 on 2021-01-08 08:51

from django.db import migrations
import csv
from django.contrib.gis.geos import fromstr

def get_calque(calque):
    if calque == 'Facile':
        return 1
    elif calque == 'Assez Difficile':
        return 2
    elif calque == 'Difficile':
        return 3
    elif calque == 'Tres Difficile':
        return 4
    elif calque == 'Extrêmement Difficile':
        return 5
    else:
        return 0

class Migration(migrations.Migration):


    def load_data(apps, _):
        DATA_FILENAME = 'eBloc Targa - Feuille 8.csv'
        Line = apps.get_model('topo', 'Line')

        jsonfile = "topo/data/" + DATA_FILENAME

        with open(jsonfile, newline='') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

            for row in spamreader:

                line = dict()

                longitude = float(row['longitude'])
                lattitude = float(row['lattitude'])
                geom = fromstr(f'POINT({longitude} {lattitude})', srid=4326)
                line['geom'] = geom
                line['name'] = row['name']
                line['incontournable'] = 0 if row['incontournable'] == '' else int(row['incontournable'])
                line['code_topo'] = row['code_topo']
                line['line_nb'] = 0 if row['ligne'] == '' else int(row['ligne'])
                line['cota'] = row['cota']
                line['calque'] = get_calque(row['calque'])
                line['da'] = bool(row['da'])
                line['da_cota'] = '' if (len(row['da']) < 2) else row['da']
                line['hauteur'] = 0 if row['haut'] == '' else float(row['haut'])
                line['inclin'] = 0 if row['inclin'] == '' else int(row['inclin'])
                line['orientation'] = row['orient']
                line['expo'] = 0 if row['expo'] == '' else int(row['expo'])
                line['trav'] = row['trav']
                line['descente'] = bool(row['descente'])
                line['morfo'] = bool(row['morfo'])
                line['reglette'] = bool(row['regle'])
                line['plans'] = bool(row['plans'])
                line['reta'] = bool(row['reta'])
                line['compression'] = bool(row['compr'])
                line['jette'] = bool(row['jette'])
                line['technique'] = bool(row['techn'])
                line['physique'] = bool(row['phis'])
                line['touche'] = bool(row['touche'])
                line['elim'] = bool(row['elim'])
                line['top'] = bool(row['top'])
                Line(**line).save()

    dependencies = [
        ('topo', '0017_auto_20210108_0844'),
    ]

    operations = [
        migrations.RunPython(load_data)

    ]
