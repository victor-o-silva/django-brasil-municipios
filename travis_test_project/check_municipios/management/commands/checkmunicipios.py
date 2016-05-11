# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
# third-party
from django.core.management.base import BaseCommand
from brasil_municipios.models import Municipio, STATES
# project
from .points_to_test import CHECK_POINTS


ALL_STATES = [choice[0] for choice in STATES]


class Command(BaseCommand):
    help = 'Checks if Municipios were created successfully'

    def add_arguments(self, parser):
        parser.add_argument(
            '--state',
            action='append',
            choices=ALL_STATES,
            help='Specify which state(s) will have its (their) municipalities'
                 ' checked. This argument can be specified multiple times.'
        )

    def handle(self, *args, **options):

        def print_out(msg):
            self.stdout.write(self.style.SUCCESS(msg))

        def print_err(msg):
            self.stderr.write(self.style.ERROR(msg))

        states = options['state']
        check_count = 0

        for check_point in CHECK_POINTS:

            if states:
                # skip points outside specified states
                if check_point['state'] not in states:
                    continue

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
                check_count += 1
        else:
            msg = 'Success: {} points checked.'.format(check_count)
            print_out('-' * 60)
            print_out(msg)
