# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# stdlib
import ftplib
import os
import shutil
import sys
import zipfile
# third party
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
# project
from ...models import Municipio


STATES = (
    'AC',  # Acre
    'AL',  # Alagoas
    'AM',  # Amazonas
    'AP',  # Amapá
    'BA',  # Bahia
    'CE',  # Ceará
    'DF',  # Distrito Federal
    'ES',  # Espírito Santo
    'GO',  # Goiás
    'MA',  # Maranhão
    'MG',  # Minas Gerais
    'MS',  # Mato Grosso do Sul
    'MT',  # Mato Grosso
    'PA',  # Pará
    'PB',  # Paraíba
    'PE',  # Pernambuco
    'PI',  # Piauí
    'PR',  # Paraná
    'RJ',  # Rio de Janeiro
    'RN',  # Rio Grande do Norte
    'RO',  # Rondônia
    'RR',  # Roraima
    'RS',  # Rio Grande do Sul
    'SC',  # Santa Catarina
    'SE',  # Sergipe
    'SP',  # São Paulo
    'TO',  # Tocantins
)

DOWNLOADS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'IBGE_DOWNLOADS'
)


def delete_municipios(print_out):
    print_out('Deleting existing Municipios.')
    count = Municipio.objects.all().delete()[0]
    print_out('{} Municipios were deleted.'.format(count))


def download_from_ibge(state, print_out):
    print_out('Downloading {} zip file from IBGE.'.format(state))
    zip_file_path = os.path.join(DOWNLOADS_PATH,
                                 '{}.zip'.format(state))

    with open(zip_file_path, 'wb') as zip_file:
        ftp = ftplib.FTP('geoftp.ibge.gov.br')
        ftp.login('anonymous', 'anonymous')
        ftp.cwd('malhas_digitais/municipio_2014/{}'.format(state))
        ftp.retrbinary(
            'RETR {}_municipios.zip'.format(state.lower()),
            zip_file.write
        )
        ftp.quit()

    return zip_file_path


def unzip_file(zip_file_path, state, print_out):
    print_out('Extracting contents from {} zip file.'.format(state))
    extracted_contents_path = os.path.join(os.path.dirname(zip_file_path),
                                           state)
    if not os.path.isdir(extracted_contents_path):
        os.mkdir(extracted_contents_path)

    zip_file = zipfile.ZipFile(zip_file_path)
    zip_file.extractall(extracted_contents_path)

    shp_file_name = [
        name for name in zip_file.namelist()
        if name.endswith('.shp')
    ][0]
    shp_file_path = os.path.join(extracted_contents_path, shp_file_name)
    return shp_file_path


def import_data(shp_file_path, state, print_out):
    print_out('Importing data for {}.'.format(state))

    # Save Municipios
    model_shp_mapping = {
        'name': 'NM_MUNICIP',
        'geocode': 'CD_GEOCMU',
        'geometry': 'MULTIPOLYGON',
    }
    LayerMapping(Municipio,
                 shp_file_path,
                 model_shp_mapping,
                 transform=False,
                 encoding='utf-8').save(strict=True)

    # Update Municipios' `state` field
    count = Municipio.objects.filter(state__isnull=True).update(state=state)
    print_out('{} Municipios were created for {}.'.format(count, state))


def fetch_data_and_create_municipios(print_out):
    # Delete existing Municipios to avoid duplication
    delete_municipios(print_out)

    # Create downloads directory
    if not os.path.isdir(DOWNLOADS_PATH):
        os.mkdir(DOWNLOADS_PATH)

    try:
        # For each state: fetch, parse and save Municipios data
        for state in STATES:
            print_out('-' * 60)
            zip_file_path = download_from_ibge(state, print_out)
            shp_file_path = unzip_file(zip_file_path, state, print_out)
            import_data(shp_file_path, state, print_out)
    finally:
        # Remove downloads directory
        shutil.rmtree(DOWNLOADS_PATH)


class Command(BaseCommand):
    help = 'Loads brazilian municipalities from IBGE'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force-delete',
            action='store_true',
            help='Force deletion of pre-existing Municipios.'
        )

    def handle(self, *args, **options):
        def print_out(data, error=False):
            if error:
                self.stderr.write(self.style.ERROR(data))
            else:
                self.stdout.write(self.style.SUCCESS(data))

        if Municipio.objects.exists() and options['force_delete'] is False:
            msg_line1 = '''
There are Municipios in the database already.
In order to import the Municipios data from IBGE, the existing records
must be deleted to avoid duplication, but that can cause data loss
if you have related objects (check
https://docs.djangoproject.com/en/dev/ref/models/querysets/#delete
for more information).'''
            msg_line2 = '''
If you are sure that you want to delete all existing Municipios and create
new ones, run this same management command with the --force-delete flag.'''
            msg = '\n'.join((msg_line1, msg_line2))
            print_out(msg, error=True)
            sys.exit(1)

        fetch_data_and_create_municipios(print_out)
