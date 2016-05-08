import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add repo root to sys.path, so brasil_municipios module can be found
REPO_ROOT = os.path.join(BASE_DIR, '..')
sys.path.append(REPO_ROOT)

SECRET_KEY = 'django-brasil-municipios-travis-test-project'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    #
    'brasil_municipios',
    'check_all_municipios'
]
MIDDLEWARE_CLASSES = []
ROOT_URLCONF = 'travis_test_project.urls'
WSGI_APPLICATION = 'travis_test_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'travis_postgis',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False
