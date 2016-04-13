# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (division, print_function, unicode_literals)

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
SENTRY_ENABLED = env.str('SENTRY_DSN', default=False)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#template-debug
THUMBNAIL_DEBUG = DEBUG

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
    os.path.join(SITE_ROOT, '../data/build'),
    os.path.join(SITE_ROOT, 'static'),
    os.path.join(SITE_ROOT, 'static_misc'),
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
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(os.path.join(SITE_ROOT, 'templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'string_if_invalid': env('TEMPLATE_STRING_IF_INVALID', default=""),
            'context_processors': [
                # Custom context processors:

                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
if not DEBUG:
    TEMPLATES[0]['APP_DIRS'] = False
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    ]
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#middleware-classes
DEFAULT_MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOCAL_MIDDLEWARE_CLASSES = [

]

THIRD_PARTY_MIDDLEWWARE_CLASSES = [
    'annoying.middlewares.StaticServe',
]

if SENTRY_ENABLED:
    DEFAULT_MIDDLEWARE_CLASSES = ['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware'] + DEFAULT_MIDDLEWARE_CLASSES

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
    # 'suit',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'django_extensions',
    'compressor',
    'django_nose',
    'annoying',
    'django_custom_500',
)

if SENTRY_ENABLED:
    THIRD_PARTY_APPS += (
        'raven.contrib.django.raven_compat',
    )

    ########## RAVEN CONFIGURATION
    # See: https://raven.readthedocs.org/en/latest/integrations/django.html
    RAVEN_CONFIG = {
        'dsn': b"%s" % env.str('SENTRY_DSN')
    }
    ########## END RAVEN CONFIGURATION

if env.bool('DEBUG_TOOLBAR', default=False):
    THIRD_PARTY_APPS += (
        'debug_toolbar',
    )

# Apps specific for this project go here.
LOCAL_APPS = (
    '{{ cookiecutter.main_app }}',
    'web',
)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

########## AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    # 'allauth.account.auth_backends.AuthenticationBackend',
)
########## END AUTHENTICATION CONFIGURATION

########## PASSWORD HASHERS
# See: https://docs.djangoproject.com/es/{{ cookiecutter.django_version }}/ref/settings/#std:setting-PASSWORD_HASHERS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]
########## END PASSWORD HASHERS

########## PASSWORD VALIDATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
########## END PASSWORD VALIDATION

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
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
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
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
        },
        'sentry': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler' if SENTRY_ENABLED else "logging.NullHandler",
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
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=False)  # Disable if SSL is not configured

SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)  # Disable if SSL is not configured
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)  # Disable if SSL is not configured
CSRF_COOKIE_HTTPONLY = True

SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)  # Disable if SSL is not configured

X_FRAME_OPTIONS = env('X_FRAME_OPTIONS', default="DENY")
########## END SECURITY CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_URL = env.email_url('EMAIL_URL', default='dummymail://')
EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
EMAIL_FILE_PATH = EMAIL_URL['EMAIL_FILE_PATH']
EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = EMAIL_URL.get('EMAIL_USE_TLS', False)

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default="no-reply@example.com")
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
########## END EMAIL CONFIGURATION

# +-----------------------------------+
# |-----------------------------------|
# || THIRD PARTY APPS CONFIGURATION  ||
# |-----------------------------------|
# +-----------------------------------+

# ########## DEBUG_TOOLBAR CONFIGURATION
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel'
]
# ########## END DEBUG_TOOLBAR CONFIGURATION

# ########## SORL CONFIGURATION
THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
# ########## END SORL CONFIGURATION

# ######### django-custom-500
CUSTOM_500_TEMPLATE = "500.html"
# ######### END django-custom-500

# ########## DJANGO SUIT CONFIGURATION
# https://django-suit.readthedocs.org/en/develop/configuration.html#header
SUIT_CONFIG = {
    'ADMIN_NAME': '{{ cookiecutter.project_name }}',
    # Set to empty string if you want to hide search from menu
    'SEARCH_URL': '',
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

# ######### ALL-AUTH
# See: https://django-allauth.readthedocs.org/en/latest/advanced.html#custom-user-models
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ######### END ALL-AUTH

# ######### DJANGO-CRISPY-FORMS
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG
# ######### END DJANGO-CRISPY-FORMS

# +------------------------------------+
# | END THIRD PARTY APPS CONFIGURATION |
# +------------------------------------+

# noinspection PyUnresolvedReferences
from app import *

try:
    from local import *
except ImportError:
    pass

if 'test' in sys.argv:
    try:
        from test import *
    except ImportError:
        pass
