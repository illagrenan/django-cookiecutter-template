# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from .base import *

# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
THUMBNAIL_DEBUG = False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

class InvalidVarException(object):
    def __mod__(self, missing):
        try:
            missing_str = unicode(missing)
        except:
            missing_str = 'Failed to create string representation'
        raise Exception('Unknown template variable %r %s' % (missing, missing_str))

    def __contains__(self, search):
        if search == '%s':
            return True
        return False


TEMPLATE_STRING_IF_INVALID = 'DEBUG WARNING: template variable [%s] is not defined'
# TEMPLATE_STRING_IF_INVALID = InvalidVarException()
# ######### END DEBUG CONFIGURATION


########## TEST RUNNER CONFIGURATION
# See: https://github.com/jbalogh/django-nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
########## END TEST RUNNER CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ cookiecutter.repo_name }}',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '{{ cookiecutter.db_user }}',
        'PASSWORD': '{{ cookiecutter.db_password }}',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}
########## END CACHE CONFIGURATION


########## APP CONFIGURATION
INSTALLED_APPS += (
    'django_nose',
)
