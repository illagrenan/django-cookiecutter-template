# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import logging
import os


class GroupWriteRotatingFileHandler(logging.handlers.RotatingFileHandler):
    # See: http://stackoverflow.com/a/6779307/752142

    def _open(self):
        prevumask = os.umask(0o002)
        # os.fdopen(os.open('/path/to/file', os.O_WRONLY, 0600))
        rtv = logging.handlers.RotatingFileHandler._open(self)
        os.umask(prevumask)
        return rtv