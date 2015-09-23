# coding=utf-8

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from django_fab_deployer.fabfile import get_tasks

for target, task_func in get_tasks():
    globals()[target] = task_func