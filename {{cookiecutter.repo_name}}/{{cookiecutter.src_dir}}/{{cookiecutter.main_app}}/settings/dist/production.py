# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

"""Production settings and globals."""

from os import environ

from .base import *

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

PREPEND_WWW = True
########## END DEBUG CONFIGURATION


# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.6/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['www.{{ cookiecutter.domain_name }}', '{{ cookiecutter.domain_name }}', "127.0.0.1", "localhost", "0.0.0.0"]
########## END HOST CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = 'no-reply@{{ cookiecutter.domain_name }}'

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-host-password
# TODO Add mail password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', "TODO")

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', "TODO")

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## CACHE CONFIGURATION
def make_key(key, key_prefix, version):
    return '{{ cookiecutter.repo_name }}' + key


# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
########## END CACHE CONFIGURATION


########## APP CONFIGURATION
# Pøidejte Raven na seznam nainstalovaných aplikací
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES += (

)
########## END MIDDLEWARE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#secret-key
# SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION



########## RAVEN CONFIGURATION
RAVEN_CONFIG = {
    'dsn': 'TODO',
}
########## END RAVEN CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ cookiecutter.repo_name }}',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '{{ cookiecutter.repo_name }}',
        'PASSWORD': 'TODO',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}
########## END DATABASE CONFIGURATION
