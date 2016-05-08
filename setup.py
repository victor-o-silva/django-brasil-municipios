# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.RST', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='django-brasil-municipios',
    version='0.1',
    author='Victor Oliveira da Silva',
    author_email='victor_o_silva@hotmail.com',
    packages=find_packages(),
    url='https://github.com/victor-o-silva/django-brasil-municipios',
    license='MIT',
    include_package_data=True,
    download_url='https://github.com/victor-o-silva/'
                 'geodjango-brasil-municipios/tarball/0.1',
    description='A GeoDjango app with all Brazilian municipalities and their '
                'geographical polygons, with data downloaded from the IBGE '
                '(Brazilian Institute of Geography and Statistics) website.',
    long_description=long_description,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)