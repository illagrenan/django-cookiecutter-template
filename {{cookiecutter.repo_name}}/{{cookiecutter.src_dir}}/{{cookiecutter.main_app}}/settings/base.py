# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function

import os
import sys
from os.path import abspath, dirname, normpath
from sys import path

import environ


env = environ.Env(DEBUG=(bool, False), )


# ######### PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = BASE_DIR = dirname(dirname(abspath(__file__)))  # .../src/main/

# Absolute filesystem path to the top-level project folder: (where manage.py is)
SITE_ROOT = dirname(DJANGO_ROOT)  # .../src/{manage.py}

# Site name:
SITE_NAME = "{{ cookiecutter.project_name }}"

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# ######### END PATH CONFIGURATION


env.read_env(os.path.join(SITE_ROOT, "..", ".env"))


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#debug
DEBUG = env('DEBUG')  # False if not in os.environ

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

TEMPLATE_STRING_IF_INVALID = env('TEMPLATE_STRING_IF_INVALID', default="")

PREPEND_WWW = env.bool('PREPEND_WWW', default=False)
# ######### END DEBUG CONFIGURATION

# ######### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#admins
ADMINS = (
    ('{{ cookiecutter.author_name }}', '{{ cookiecutter.email }}'),
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#managers
MANAGERS = ADMINS
# ######### END MANAGER CONFIGURATION


# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#databases
DATABASES = {
    'default': env.db(),  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}
# ######### END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#time-zone
TIME_ZONE = 'Europe/Prague'

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#language-code
LANGUAGE_CODE = 'cs'

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#use-tz
USE_TZ = False

ugettext = lambda s: s  # dummy ugettext function, as django's docs say

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#languages
LANGUAGES = (
    ('cs', ugettext('Czech')),
)


LOCALE_PATHS = (
    os.path.join(SITE_ROOT, '../data/locale'),  # Assuming SITE_ROOT is where your manage.py file is
)

MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#media-root
MEDIA_ROOT = os.path.join(SITE_ROOT, '../data/media')

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#static-root
STATIC_ROOT = os.path.join(SITE_ROOT, '../data/static')

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#secret-key
# Note: This key only used for development and testing.
# TODO Generate unique SECRET_KEY
SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = ()
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See:  https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#template-context-processors
DEFAULT_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

THIRD_PARTY_CONTEXT_PROCESSORS = (

)

LOCAL_CONTEXT_PROCESSORS = (

)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_CONTEXT_PROCESSORS + THIRD_PARTY_CONTEXT_PROCESSORS + LOCAL_CONTEXT_PROCESSORS

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(os.path.join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#middleware-classes
DEFAULT_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

THIRD_PARTY_MIDDLEWWARE_CLASSES = (
    'annoying.middlewares.StaticServe',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + THIRD_PARTY_MIDDLEWWARE_CLASSES
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#root-urlconf
ROOT_URLCONF = '{{ cookiecutter.main_app }}.urls'
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'django_extensions',
    'compressor',
    'django_nose',
    'annoying',
    'django_custom_500'
)

if env.str('SENTRY_DSN', default=False):
    import raven

    THIRD_PARTY_APPS += (
        'raven.contrib.django',
    )

    ########## RAVEN CONFIGURATION
    # See: https://raven.readthedocs.org/en/latest/integrations/django.html
    RAVEN_CONFIG = {
        'dsn': env('SENTRY_DSN')
    }
    ########## END RAVEN CONFIGURATION

if env.bool('DEBUG_TOOLBAR', default=False):
    THIRD_PARTY_APPS += (
        'debug_toolbar',
    )

# Apps specific for this project go here.
LOCAL_APPS = (
    'web',
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

########## CACHES CONFIGURATION
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#caches
CACHES = {
    'default': env.cache(default="dummycache://"),
}
########## END CACHES CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'development_debug': {
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
            'filename': os.path.os.path.join(DJANGO_ROOT, '../../log/django-dev-debug.log'),
            'level': 'DEBUG',
            'class': '{{ cookiecutter.main_app }}.settings.log.handlers.GroupWriteRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'production_errors': {
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
            'filename': os.path.os.path.join(DJANGO_ROOT, '../../log/django-error.log'),
            'level': 'ERROR',
            'class': '{{ cookiecutter.main_app }}.settings.log.handlers.GroupWriteRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
        'sentry': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'ERROR',
        },
        'sentry': {
            'handlers': ['sentry'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['production_errors'],
            'level': 'DEBUG',
            'propagate': False
        },
        '': {
            'handlers': ['development_debug'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


# ########## SESSION CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#sessions
CACHE_MIDDLEWARE_KEY_PREFIX = SITE_NAME
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
########## END SESSION CONFIGURATION


# ########## SECURITY CONFIGURATION
# http://django-secure.readthedocs.org/en/v0.1.2/
SESSION_COOKIE_SECURE = False
SECURE_FRAME_DENY = False
SECURE_BROWSER_XSS_FILTER = False
SESSION_COOKIE_HTTPONLY = True
########## END SECURITY CONFIGURATION

########## EMAIL CONFIGURATION
# {
# u'EMAIL_HOST_PASSWORD': None,
# u'EMAIL_BACKEND': u'django.core.mail.backends.dummy.EmailBackend',
# u'EMAIL_HOST_USER': None,
#     u'EMAIL_USE_TLS': False,
#     u'EMAIL_PORT': None,
#     u'EMAIL_FILE_PATH': u'',
#     u'EMAIL_HOST': None
# }


EMAIL_URL = env.email_url('EMAIL_URL', default='dummymail://')
EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
EMAIL_FILE_PATH = EMAIL_URL['EMAIL_FILE_PATH']
EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = EMAIL_URL['EMAIL_USE_TLS']

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default="no-reply@example.com")
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
########## END EMAIL CONFIGURATION

# +-----------------------------------+
# |-----------------------------------|
# || THIRD PARTY APPS CONFIGURATION  ||
# |-----------------------------------|
# +-----------------------------------+


# ######### django-custom-500
CUSTOM_500_TEMPLATE = "500.html"
# ######### END django-custom-500

# ######### DJANGO-MARKUPMIRROR
MARKUPMIRROR_DEFAULT_MARKUP_TYPE = 'markdown'
# https://pythonhosted.org/Markdown/extensions/#officially-supported-extensions
MARKUPMIRROR_MARKDOWN_EXTENSIONS = ['tables', 'smart_strong', 'smarty', 'attr_list', 'headerid(level=2)']
# ######### END DJANGO-MARKUPMIRROR


# ########## GRAPELLI CUSTOMIZATIONS
# http://django-grappelli.readthedocs.org/en/latest/customization.html
GRAPPELLI_ADMIN_TITLE = "{{ cookiecutter.project_name }}"
########## END GRAPELLI CUSTOMIZATIONS

# ########## DJANGO SUIT CONFIGURATION
# https://django-suit.readthedocs.org/en/develop/configuration.html#header
SUIT_CONFIG = {
    'ADMIN_NAME': '{{ cookiecutter.project_name }}'
}
########## END DJANGO SUIT CONFIGURATION

# ########## DJANGO COMPRESSOR CONFIGURATION
# Boolean that decides if compression should also be done outside of the
# request/response loop – independent from user requests.
# This allows to pre-compress CSS and JavaScript files and works just
# like the automatic compression with the {% raw %}{% compress %}{% endraw %} tag.
# https://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True
# ########## END DJANGO COMPRESSOR CONFIGURATION

# ########## DJANGO-NOSE CONFIGURATION
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--nocapture',
    '--nologcapture'
]
# ########## END DJANGO-NOSE CONFIGURATION

# +------------------------------------+
# | END THIRD PARTY APPS CONFIGURATION |
# +------------------------------------+

# noinspection PyUnresolvedReferences
from app import *

try:
    from local import *
except ImportError:
    pass

if 'test' in sys.argv or 'jenkins' in sys.argv:
    try:
        from test import *
    except ImportError:
        pass
