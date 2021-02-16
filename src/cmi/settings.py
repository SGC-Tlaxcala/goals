from unipath import Path
import os

PROJECT_DIR = Path(__file__).ancestor(2)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_URL = '/assets/'
MEDIA_URL  = '/media/'
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)
TEMPLATE_DIRS = (
    'templates'
)

DEBUG = True

TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = ['10.69.0.68', ]

import django.conf.global_settings as DEFAULT_SETTINGS
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap_toolkit',
    'tinymce',
    'watson',
    'core',
    'metas',
    'docs'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cmi.urls'

WSGI_APPLICATION = 'cmi.wsgi.application'
SECRET_KEY = 'p5&6htp*4ju9-00_0wfr!92-rdfl(awgj5w6+ad@5pomdi%sdb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'goals',
        'USER': 'javier',
        'PASSWORD': 'santo97',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'Mexico/General'
USE_I18N = True
USE_L10N = True
USE_TZ = False

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = "core.Pipol"

WATSON_BACKEND="watson.backends.PostgresSearchBackend"
