# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django_fab_deployer.fabfile import get_tasks

for target, task_func in get_tasks():
    globals()[target] = task_func
