"""
Django settings for clinic project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from django.utils.translation import ugettext_lazy as _

BASE_DIR = dirname(dirname(abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_q4j2$ur6ce*4z(m-jy2rm1gn9(x#d!mbpy1td-2ki4kim1g=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CLINIC_APPS = (
    # Useful template tags:
    'django.contrib.humanize',

    # Static file management:
    'compressor',

    # Admin docs
    'django.contrib.admindocs',

    # Thumbnails
    'sorl.thumbnail',

    # From frontend
    'django_filters',
    'django_select2',

    # Frontend user app
    'home',
    'home.templatetags',
    'home.middleware.force_default_language',
)

INSTALLED_APPS = DJANGO_APPS + CLINIC_APPS

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'smtp.gmail.com'

# Port for sending e-mail.
EMAIL_PORT = 587

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

########## END EMAIL CONFIGURATION`

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

MIDDLEWARE_CLASSES = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',
    # 'home.middleware.force_default_language.ForceDefaultLanguageMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'clinic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'clinic.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'clinic_dev',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEFAULT_INDEX_TABLESPACE = ''

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ja' #'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'

########## MEDIA FILE CONFIGURATION
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL='/media/'

########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
def custom_show_toolbar(request):
    return True  # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar
}
INSTALLED_APPS += (
    'debug_toolbar',
)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION

############## SELECT2 CONFIG
SELECT2_JS = u'//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/js/select2.min.js'
SELECT2_CSS = u'//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/css/select2.min.css'
SELECT2_CACHE_BACKEND = u'default'

############ I18N
LANGUAGES = (
    ('en', _('English')),
    ('ja', _('Japanese')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
