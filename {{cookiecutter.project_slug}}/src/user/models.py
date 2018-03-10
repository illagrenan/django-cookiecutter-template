# -*- encoding: utf-8 -*-
# ! python3

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy

from user.managers import UserManager


class {{ cookiecutter.project_slug|capitalize }}User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(ugettext_lazy('email address'), blank=False, null=False, unique=True, db_index=True, max_length=512)
    first_name = models.CharField(ugettext_lazy('first name'), max_length=255, blank=True)
    last_name = models.CharField(ugettext_lazy('last name'), max_length=255, blank=True)
    is_staff = models.BooleanField(
        ugettext_lazy('staff status'),
        default=False,
        help_text=ugettext_lazy('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text=ugettext_lazy(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(ugettext_lazy('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = ugettext_lazy('user')
        verbose_name_plural = ugettext_lazy('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
