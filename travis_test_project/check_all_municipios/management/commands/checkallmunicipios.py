# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
# third-party
from django.core.management.base import BaseCommand
from brasil_municipios.models import Municipio
# project
from .points_to_test import CHECK_POINTS


class Command(BaseCommand):
    help = 'Checks if ALL Municipios were created successfully'

    def handle(self, *args, **options):

        def print_out(msg):
            self.stdout.write(self.style.SUCCESS(msg))

        def print_err(msg):
            self.stderr.write(self.style.ERROR(msg))

        for check_point in CHECK_POINTS:
            try:
                point = check_point['point']
                m = Municipio.objects.get(geometry__contains=point)
                assert m.name == check_point['municipio'], \
                    'Invalid name: expected {} got {}'.format(
                        check_point['municipio'],
                        m.name
                )
                assert m.geocode == check_point['geocode'], \
                    'Invalid geocode: expected {} got {}'.format(
                        check_point['geocode'],
                        m.geocode
                )
                assert m.state == check_point['state'], \
                    'Invalid state: expected {} got {}'.format(
                        check_point['state'],
                        m.state
                )
            except (
                Municipio.DoesNotExist,
                Municipio.MultipleObjectsReturned,
                AssertionError
            ) as exception:
                msg = 'Failed when checking {} ; exception: {}'.format(
                    repr(check_point),
                    repr(exception)
                )
                print_err('-' * 60)
                print_err(msg)
                sys.exit(1)
        else:
            msg = 'Success: {} points checked.'.format(len(CHECK_POINTS))
            print_out('-' * 60)
            print_out(msg)
