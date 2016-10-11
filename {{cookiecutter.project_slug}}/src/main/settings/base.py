# -*- encoding: utf-8 -*-
# ! python3

import os
import sys

import environ

env = environ.Env(DEBUG=(bool, False), )

# PATH CONFIGURATION
# ------------------------------------------------------------------------------
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # .../src/main/

# Absolute filesystem path to the top-level project folder: (where manage.py is)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)  # .../src/{manage.py}

# Add our project to our pythonpath, this way we don't need to type our project name in our dotted import paths:
sys.path.append(DJANGO_ROOT)
env.read_env(os.path.join(SITE_ROOT, "..", ".env"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
DEBUG = env('DEBUG')  # False if not in os.environ
SENTRY_ENABLED = env.str('SENTRY_DSN', default=False)
DEBUG_TOOLBAR_ENABLED = env.bool('DEBUG_TOOLBAR', default=False)
THUMBNAIL_DEBUG = DEBUG
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ADMINS CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('{{ cookiecutter.author_name }}', '{{ cookiecutter.email }}'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db(),  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
SITE_NAME = "{{ cookiecutter.project_slug }}"
REDIS_PREFIX = env('REDIS_PREFIX')  # Keep this unique! This prefix is used for: django-redis and celery
PREPEND_WWW = env.bool('PREPEND_WWW', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = 'Europe/Prague'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'cs'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

ugettext = lambda s: s  # dummy ugettext function, as django's docs say

# See: https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = (
    ('cs', ugettext('Czech')),
)

LOCALE_PATHS = (
    os.path.join(SITE_ROOT, '../data/locale'),  # Assuming SITE_ROOT is where your manage.py file is
)

MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(SITE_ROOT, '../data/media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(SITE_ROOT, '../data/static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, '../data/build'),
    os.path.join(SITE_ROOT, 'static'),
    os.path.join(SITE_ROOT, 'static_misc'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# TODO Generate unique SECRET_KEY
SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = ()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'string_if_invalid': env('TEMPLATE_STRING_IF_INVALID', default=""),
            'context_processors': [
                # Custom context processors:
                # ...
                # ...

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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/topics/http/middleware/
DEFAULT_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOCAL_MIDDLEWARE = [
]

THIRD_PARTY_MIDDLEWWARE = [
]

if DEBUG_TOOLBAR_ENABLED:
    DEFAULT_MIDDLEWARE = ['main.middleware.AtopdedTo110DebugMiddleware'] + DEFAULT_MIDDLEWARE

MIDDLEWARE = DEFAULT_MIDDLEWARE + LOCAL_MIDDLEWARE + THIRD_PARTY_MIDDLEWWARE
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# URL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'main.urls'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
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
]

THIRD_PARTY_APPS = [
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'django_extensions',
    'compressor',
    'annoying',
    'django_custom_500',
]

if SENTRY_ENABLED:
    THIRD_PARTY_APPS += [
        'raven.contrib.django.raven_compat',
    ]

    # RAVEN CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://raven.readthedocs.org/en/latest/integrations/django.html
    RAVEN_CONFIG = {
        'dsn': env.str('SENTRY_DSN')
    }
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if DEBUG_TOOLBAR_ENABLED:
    THIRD_PARTY_APPS += [
        'debug_toolbar',
    ]

# Apps specific for this project go here.
LOCAL_APPS = [
    'main',
    'web',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    # 'allauth.account.auth_backends.AuthenticationBackend',
]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PASSWORD HASHERS
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/es/dev/ref/settings/#std:setting-PASSWORD_HASHERS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CACHES CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches

REDIS_URL = env.str('REDIS_URL', default=False)
_is_cache_url_set = env.str('CACHE_URL', default=False)

if REDIS_URL and not _is_cache_url_set:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL, # redis://@localhost:6379/7
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            "KEY_PREFIX": REDIS_PREFIX
        }
    }
else:
    CACHES = {
        'default': env.cache(default="dummycache://"),
    }
CACHE_MIDDLEWARE_KEY_PREFIX = REDIS_PREFIX
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(module)s - %(funcName)s:%(lineno)s] %(message)s",
            'datefmt': "%d.%m.%Y %H:%M:%S"
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
        'debug_file': {
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
            'filename': os.path.join(DJANGO_ROOT, '../../log/django-DEBUG-debug-true.log'),
            'level': 'DEBUG',
            'class': 'main.settings.log.handlers.GroupWriteRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
        },
        'production_file': {
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
            'filename': os.path.join(DJANGO_ROOT, '../../log/django-INFO-debug-false.log'),
            'level': 'INFO',
            'class': 'main.settings.log.handlers.GroupWriteRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'sentry': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler' if SENTRY_ENABLED else "logging.NullHandler",
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        }
    },
    'loggers': {
        # django is the catch-all logger. No messages are posted directly to this logger.
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
            'handlers': ['production_file'],
            'level': 'DEBUG',
            'propagate': True
        },
        # Catch-all logger
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# WSGI CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SESSION CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SECURITY CONFIGURATION
# ------------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=False)  # Disable if SSL is not configured

SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)  # Disable if SSL is not configured
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)  # Disable if SSL is not configured
CSRF_COOKIE_HTTPONLY = True

SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)  # Disable if SSL is not configured

X_FRAME_OPTIONS = env('X_FRAME_OPTIONS', default="DENY")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
if env.bool('USE_ANYMAIL', default=False):
    ANYMAIL = {
        "MAILGUN_API_KEY": env.str('MAILGUN_API_KEY'),
        "MAILGUN_SENDER_DOMAIN": env.str('MAILGUN_SENDER_DOMAIN'),
    }
    EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
else:
    EMAIL_URL = env.email_url('EMAIL_URL', default='dummymail://')
    EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
    EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
    EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
    EMAIL_FILE_PATH = EMAIL_URL['EMAIL_FILE_PATH']
    EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']
    EMAIL_USE_TLS = EMAIL_URL.get('EMAIL_USE_TLS', False)

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default="no-reply@{{ cookiecutter.domain_name }}")
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DEBUG_TOOLBAR CONFIGURATION
# ------------------------------------------------------------------------------
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

# We're using Explicit setup, see: https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#explicit-setup
DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = env.list('INTERNAL_IPS', default=[])
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SORL CONFIGURATION
# ------------------------------------------------------------------------------
THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_KEY_PREFIX = REDIS_PREFIX
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CUSTOM 500 CONFIGURATION
# ------------------------------------------------------------------------------
CUSTOM_500_TEMPLATE = "500.html"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DJANGO SUIT CONFIGURATION
# ------------------------------------------------------------------------------
# https://django-suit.readthedocs.org/en/develop/configuration.html#header
SUIT_CONFIG = {
    'ADMIN_NAME': '{{ cookiecutter.project_slug }}',
    # Set to empty string if you want to hide search from menu
    'SEARCH_URL': '',
}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DJANGO COMPRESSOR CONFIGURATION
# ------------------------------------------------------------------------------
# Boolean that decides if compression should also be done outside of the
# request/response loop – independent from user requests.
# This allows to pre-compress CSS and JavaScript files and works just
# like the automatic compression with the {% raw %}{% compress %}{% endraw %} tag.
# https://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TEST CONFIGURATION
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ALL-AUTH CONFIGURATION
# ------------------------------------------------------------------------------
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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DJANGO-CRISPY-FORMS CONFIGURATION
# ------------------------------------------------------------------------------
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# noinspection PyUnresolvedReferences
from main.settings.app import *

try:
    from local import *
except ImportError:
    pass
