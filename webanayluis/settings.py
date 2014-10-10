#!env/bin/python
# -*- coding: utf-8 -*-

"""
Django settings for webanayluis project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9^sz6@97k+@l@^i+g3f3c42i^llv#g^k1p!oa)p%m5kjc^9pk1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['ww2.anayluistango.com.ar', 'www.anayluistango.com.ar',
                 'anayluistango.com.ar', '127.0.0.1', 'localhost']


ADMINS = (
    (u'Guillermo Nuñez', 'gui.nunez@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'localeurl',
    'django.contrib.admin',
    # 'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar.apps.DebugToolbarConfig',
    'contact_form',
    'ckeditor',
    'file_resubmit',
    'imagekit',
    'contenidos',
)

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webanayluis.urls'

WSGI_APPLICATION = 'webanayluis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "file_resubmit": {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        "LOCATION": '/tmp/file_resubmit/'
    },
}


INTERNAL_IPS = ("127.0.0.1",)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

LANGUAGES = (('es', u'Español'),
             ('en', u'English'),)

LOCALE_PATHS = (
    os.path.join(os.path.dirname(BASE_DIR), 'locale'),
    'locale'
)

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_INDEPENDENT_PATHS = (
    r'^/admin/',
    r'^/static/',
    r'^/css/',
    r'^/img/',
    r'^/js/',
    r'^/fonts/',
    r'^/ckeditor/',
    r'^/admin/',
    r'^/media/',
    r'^/maquetado/',
    r'^/files/',
    #r'^/contacto/',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MAQUETADO_ROOT = os.path.join(BASE_DIR, "maquetado")

PAGINATE_BY = 24

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Styles', 'Format',
             '-', 'TextColor', 'BGColor',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Image', 'Youtube', 'Iframe', 'Flash', 'Table', 'leaflet',
             '-', 'BulletedList', 'NumberedList',
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar',
             '-', 'Source',
             ]
        ],
        'language': 'es',
        'scayt_sLang': 'es_ES',
        'wsc_lang': 'es_ES',
        'extraAllowedContent': 'iframe[src,width,height,frameborder,style]',
        'width': '100%',
        'extraPlugins': 'youtube,widget,lineutils,leaflet',
        'youtube_width': '617',
    },
}


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'server.salida.mendoza'
EMAIL_HOST_PASSWORD = 'UxtyYFf0'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'server.salida.mendoza@gmail.com'


DEBUG_TOOLBAR_PATCH_SETTINGS = False

try:
    from settings_local import *
except ImportError:
    pass
