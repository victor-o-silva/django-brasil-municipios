# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# third-party
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
# project
from ...models import Municipio


POINTS_TO_CHECK = [
    {
        'point': Point(-67.809244, -9.971425),
        'name': 'Museu da Borracha',
        'municipio': 'RIO BRANCO', 'state': 'AC'
    },
    {
        'point': Point(-35.759121, -9.670764),
        'name': 'Estádio Rei Pelé',
        'municipio': 'MACEIÓ', 'state': 'AL'
    },
    {
        'point': Point(-51.077743, 0.000729),
        'name': 'Marco Zero',
        'municipio': 'MACAPÁ', 'state': 'AP'
    },
    {
        'point': Point(-60.004136, -3.080706),
        'name': 'Parque do Mindu',
        'municipio': 'MANAUS', 'state': 'AM'
    },
    {
        'point': Point(-38.520235, -3.721304),
        'name': 'Centro Dragão do Mar de Arte e Cultura',
        'municipio': 'FORTALEZA', 'state': 'CE'
    },
    {
        'point': Point(-47.861297, -15.800666),
        'name': 'Praça dos Três Poderes',
        'municipio': 'BRASÍLIA', 'state': 'DF'
    },
    {
        'point': Point(-40.332855, -20.295689),
        'name': 'Parque da Fonte Grande',
        'municipio': 'VITÓRIA', 'state': 'ES'
    },
    {
        'point': Point(-49.252236, -16.666670),
        'name': 'Parque Mutirama',
        'municipio': 'GOIÂNIA', 'state': 'GO'
    },
    {
        'point': Point(-44.304393, -2.527857),
        'name': 'Catedral de São Luís do Maranhão',
        'municipio': 'SÃO LUÍS', 'state': 'MA'
    },
    {
        'point': Point(-56.096098, -15.601752),
        'name': 'Igreja do Bom Despacho',
        'municipio': 'CUIABÁ', 'state': 'MT'
    },
    {
        'point': Point(-54.573414, -20.453387),
        'name': 'Parque das Nações Indígenas',
        'municipio': 'CAMPO GRANDE', 'state': 'MS'
    },
    {
        'point': Point(-43.972732, -19.861950),
        'name': 'Estádio do Mineirinho',
        'municipio': 'BELO HORIZONTE', 'state': 'MG'
    },
    {
        'point': Point(-48.505950, -1.464250),
        'name': 'Mangal das Garças',
        'municipio': 'BELÉM', 'state': 'PA'
    },
    {
        'point': Point(-34.876560, -7.114048),
        'name': 'Parque Arruda Câmara',
        'municipio': 'JOÃO PESSOA', 'state': 'PB'
    },
    {
        'point': Point(-49.266944, -25.410135),
        'name': 'Museu Oscar Niemeyer',
        'municipio': 'CURITIBA', 'state': 'PR'
    },
    {
        'point': Point(-34.904768, -8.036893),
        'name': 'Parque da Jaqueira',
        'municipio': 'RECIFE', 'state': 'PE'
    },
    {
        'point': Point(-42.814185, -5.095200),
        'name': 'Casa da Cultura de Teresina',
        'municipio': 'TERESINA', 'state': 'PI'
    },
    {
        'point': Point(-43.210783, -22.951570),
        'name': 'Cristo Redentor',
        'municipio': 'RIO DE JANEIRO', 'state': 'RJ'
    },
    {
        'point': Point(-35.204717, -5.779507),
        'name': 'Teatro Alberto Maranhão',
        'municipio': 'NATAL', 'state': 'RN'
    },
    {
        'point': Point(-51.231762, -30.029026),
        'name': 'Museu de Arte do Rio Grande do Sul',
        'municipio': 'PORTO ALEGRE', 'state': 'RS'
    },
    {
        'point': Point(-63.901167, -8.714592),
        'name': 'Aeroporto Internacional de porto Velho',
        'municipio': 'PORTO VELHO', 'state': 'RO'
    },
    {
        'point': Point(-60.678048, 2.825736),
        'name': 'Praça das Águas',
        'municipio': 'BOA VISTA', 'state': 'RR'
    },
    {
        'point': Point(-48.517036, -27.581165),
        'name': 'Parque do Manguezal do Itacorubi',
        'municipio': 'FLORIANÓPOLIS', 'state': 'SC'
    },
    {
        'point': Point(-46.656020, -23.561488),
        'name': 'Museu de Arte de São Paulo',
        'municipio': 'SÃO PAULO', 'state': 'SP'
    },
    {
        'point': Point(-37.053942, -10.960207),
        'name': 'Parque dos Cajueiros',
        'municipio': 'ARACAJU', 'state': 'SE'
    },
    {
        'point': Point(-48.357790, -10.294264),
        'name': 'Aeroporto de Palmas',
        'municipio': 'PALMAS', 'state': 'TO'
    },
]


class Command(BaseCommand):
    help = 'Checks if Municipios were created successfully'

    def handle(self, *args, **options):

        def print_out(msg):
            self.stdout.write(self.style.SUCCESS(msg))

        def print_err(msg):
            self.stderr.write(self.style.ERROR(msg))

        error_count = 0
        for check_point in POINTS_TO_CHECK:
            try:
                point = check_point['point']
                m = Municipio.objects.get(geometry__contains=point)
                assert m.name == check_point['municipio']
                assert m.state == check_point['state']
                msg = 'Point "{}" found in {} ({}).'.format(
                    check_point['name'],
                    m.name,
                    m.state
                )
                print_out(msg)
            except Municipio.DoesNotExist:
                error_count += 1
                msg = 'Found no Municipio containing {} ({})'.format(
                    point.wkt,
                    check_point['name']
                )
                print_err(msg)
            except Municipio.MultipleObjectsReturned:
                error_count += 1
                msg = 'Found multiple Municipios containing {} ({})'.format(
                    point.wkt,
                    check_point['name']
                )
                print_err(msg)
            except AssertionError:
                error_count += 1
                msg = 'Found Municipio containing {} ({}), but with ' \
                      'unexpected values'.format(point.wkt,
                                                 check_point['name'])
                print_err(msg)

        if error_count > 0:
            msg = 'Fail: errors when checking {} of {} points.'.format(
                error_count,
                len(POINTS_TO_CHECK)
            )
            print_err('-' * 60)
            print_err(msg)
        else:
            msg = 'Success: {} of {} points checked.'.format(
                len(POINTS_TO_CHECK),
                len(POINTS_TO_CHECK)
            )
            print_out('-' * 60)
            print_out(msg)
