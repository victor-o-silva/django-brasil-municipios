.. |project-name| replace:: **django-brasil-municipios**

==============
|project-name|
==============

This is the documentation for |project-name|, a `GeoDjango <https://docs.djangoproject.com/en/dev/ref/contrib/gis/>`_ app with all Brazilian municipalities and their geographical polygons, with data downloaded from the IBGE (Brazilian Institute of Geography and Statistics) `website <http://downloads.ibge.gov.br/downloads_geociencias.htm>`_.

*********
Demo Code
*********

::

    >>> from django.contrib.gis.geos import Point
    >>> from brasil_municipios.models import Municipio
    >>>
    >>> cristo_redentor = Point(-43.210493, -22.951906, srid=4326)
    >>> municipio_cristo = Municipio.objects.get(geometry__contains=cristo_redentor)
    >>> municipio_cristo.name, municipio_cristo.geocode, municipio_cristo.state
    ('RIO DE JANEIRO', '3304557', 'RJ')
    

************
Installation
************

First of all, your Django project must meet the `requirements for GeoDjango <https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/>`_, including a spatial database and geospatial libraries.

-----------
Install app
-----------

You can install |project-name| in your environment from the `Python Package Index <https://pypi.python.org/pypi>`_::
    
    $ pip install django-brasil-municipios
    
---------------
Update settings
---------------

On your project's settings, add ``'brasil_municipios'`` to your
`INSTALLED_APPS list <https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps>`_.

*********
Load data
*********

First, run |project-name|'s migrations in order to create the app's tables in the database::
    
    $ python manage.py migrate brasil_municipios

Then, you can run the following command to actually download the Brazilian municipalities' data::
    
    $ python manage.py loadmunicipios

That will take some time to complete. Once the data is successfully imported, you can start a `Django shell <https://docs.djangoproject.com/en/dev/ref/django-admin/#shell>`_ and run the example shown before in the `Demo Code`_.

************
Django Admin
************

If your project uses `Django Admin <https://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_, |project-name| will appear in it, and you will be able to view the municipalities in a map:

.. image:: _static/Admin_001.png
   :align: center

.. image:: _static/Admin_002.png
   :align: center

.. image:: _static/Admin_003.png
   :align: center

.. image:: _static/Admin_004.png
   :align: center

.. image:: _static/Admin_005.png
   :align: center

.. Contents:
.. 
.. .. toctree::
..    :maxdepth: 2