# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# third-party
from django.core.management.base import BaseCommand
from brasil_municipios.models import Municipio


class Command(BaseCommand):
    help = 'Deletes all Municipios'

    def handle(self, *args, **options):
        Municipio.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Municipios deleted.'))
