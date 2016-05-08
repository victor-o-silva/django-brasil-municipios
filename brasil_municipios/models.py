# third-party
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Municipio(models.Model):
    name = models.CharField(max_length=60)
    geocode = models.CharField(max_length=7)
    state = models.CharField(max_length=2, null=True)
    geometry = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
