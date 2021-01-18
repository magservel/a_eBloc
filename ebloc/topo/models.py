from django.db import models

# Create your models here.

from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.core.validators import MinValueValidator, MaxValueValidator

orientation_choices = [
    ('n', 'Nord'),
    ('s', 'Sud'),
    ('e', 'Est'),
    ('o', 'Ouest'),
    ('ne', 'Nord-Est'),
    ('se', 'Sud_Est'),
    ('no', 'Nord-Ouest'),
    ('so', 'Sud-Ouest'),

]


class Other(models.Model):
    other_type_choices = [
        (1, 'Parking'),
        (2, 'Camping'),
    ]

    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=other_type_choices)
    geom = models.PointField()
    objects = GeoManager()


class Sentier(models.Model):
    name = models.CharField(max_length=50, blank=True)
    geom = models.LineStringField()
    objects = GeoManager()


class Sector(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    geom = models.PolygonField(srid=4326)
    forgiven = models.BooleanField(default=False)
    objects = GeoManager()


class Bloc(models.Model):
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.SET(0))
    geom = models.PointField(null=True)
    objects = GeoManager()


class Line(models.Model):

    calques_choices = [
        (0, 'UNKNOWN'),
        (1, 'FACILE'),
        (2, 'DIFFICILE'),
        (3, 'ASSEZ_DIFFICILE'),
        (4, 'TRES_DIFFICILE'),
        (5, 'EXTREMEMENT_DIFFICILE'),
    ]

    incontournable_choices = [
        (0, 'Aucun'),
        (1, 'Secteur'),
        (2, 'Site'),
    ]

    geom = models.PointField(null=True)
    objects = GeoManager()
    name = models.CharField(max_length=100, blank=True)
    bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE, null=True)
    incontournable = models.IntegerField(choices=incontournable_choices, default=0)
    code_topo = models.CharField(max_length=10, blank=True)
    line_nb = models.IntegerField(default=0)
    cota = models.CharField(max_length=10, blank=True)
    calque = models.IntegerField(choices=calques_choices, default=0)
    da = models.BooleanField(default=False)
    da_cota = models.CharField(max_length=10, blank=True)
    hauteur = models.FloatField(default=0)
    inclin = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    orientation = models.CharField(max_length=2, choices=orientation_choices, blank=True)
    expo = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], default=0)
    trav = models.CharField(max_length=3, blank=True)
    descente = models.BooleanField(default=False)
    morfo = models.BooleanField(default=False)
    reglette = models.BooleanField(default=False)
    plans = models.BooleanField(default=False)
    reta = models.BooleanField(default=False)
    compression = models.BooleanField(default=False)
    jette = models.BooleanField(default=False)
    technique = models.BooleanField(default=False)
    physique = models.BooleanField(default=False)
    touche = models.BooleanField(default=False)
    elim = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    obs_fr = models.CharField(max_length=1000, blank=True)
    obs_es = models.CharField(max_length=1000, blank=True)
    obs_en = models.CharField(max_length=1000, blank=True)
    obs_cat = models.CharField(max_length=1000, blank=True)
    da_nom = models.CharField(max_length=50, blank=True)
    ext = models.CharField(max_length=5, blank=True)
    var = models.CharField(max_length=5, blank=True)
    avis_1 = models.CharField(max_length=5, blank=True)
    avis_2 = models.CharField(max_length=5, blank=True)
    annee = models.CharField(max_length=5, blank=True)
    ouvert = models.CharField(max_length=50, blank=True)
    first_ascent = models.CharField(max_length=50, blank=True)

    @property
    def printInfo(self):
        html = self.name
        return print_info_gen(html)


def print_info_gen(html):
    res = """
                <h1 class="sidebar-header"> Infos <span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
                <p> """ + html + """
                </p>
    """
    return res


class Photo(models.Model):
    target_choices = [
        (0, 'Bloc'),
        (1, 'Ligne'),
        (2, 'Artistique'),
    ]
    target_type = models.IntegerField(choices=target_choices, default=0)
    target_bloc = models.ForeignKey(Bloc, on_delete=models.CASCADE, null=True)
    target_line = models.ForeignKey(Line, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='photo/.')
    orientation = models.CharField(max_length=2, choices=orientation_choices)
    number = models.IntegerField(default=0)
    note = models.IntegerField(default=0)
