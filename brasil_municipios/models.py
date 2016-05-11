# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# third-party
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


STATES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins'),
)


@python_2_unicode_compatible
class Municipio(models.Model):
    name = models.CharField(max_length=60)
    geocode = models.CharField(max_length=7)
    state = models.CharField(max_length=2, null=True, choices=STATES)
    geometry = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
