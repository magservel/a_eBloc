# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from django.contrib.gis.geos import fromstr
import os
# Press the green button in the gutter to run the script.


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


def get_line_data():
    DATA_FILENAME = 'eBloc Targa - Feuille 8.csv'

    jsonfile = "ebloc/topo/data/" + DATA_FILENAME

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


def set_photo_to_line():
    dir_path = 'ebloc/topo/static/img/photo/line'
    photos = os.listdir(dir_path)
    print(photos)
    for p in photos:
        print(p)
        # target_type = 1
        # target_line = 00
        # photo = p


if __name__ == '__main__':
    set_photo_to_line()
