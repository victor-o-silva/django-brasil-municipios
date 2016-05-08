# third-party
from django.contrib.gis import admin
# project
from .models import Municipio


class MunicipioAdmin(admin.OSMGeoAdmin):
    list_filter = ['state']
    list_display = ['state', 'id', 'geocode', 'name']
    list_display_links = ['id', 'geocode', 'name']
    search_fields = ['name', 'geocode']
    ordering = ['state', 'name']
    modifiable = False

admin.site.register(Municipio, MunicipioAdmin)
