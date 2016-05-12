# third-party
from django.contrib.gis import admin
from django.core.exceptions import ImproperlyConfigured
# project
from .models import Municipio


# Create Admin classes dynamically to avoid code repetition

members = {
    'list_filter': ['state'],
    'list_display': ['state', 'id', 'geocode', 'name'],
    'list_display_links': ['id', 'geocode', 'name'],
    'search_fields': ['name', 'geocode'],
    'ordering': ['state', 'name'],
    'modifiable': False,
}

MunicipioOSMGeoAdmin = type('MunicipioOSMGeoAdmin',
                            (admin.OSMGeoAdmin,),
                            members)

MunicipioGeoModelAdmin = type('MunicipioGeoModelAdmin',
                              (admin.GeoModelAdmin,),
                              members)

try:
    admin.site.register(Municipio, MunicipioOSMGeoAdmin)
except ImproperlyConfigured:
    # OSMGeoAdmin requirements not met; fallback to standard GeoModelAdmin
    admin.site.register(Municipio, MunicipioGeoModelAdmin)
