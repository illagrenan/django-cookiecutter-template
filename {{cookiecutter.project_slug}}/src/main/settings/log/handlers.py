# -*- encoding: utf-8 -*-
# ! python3

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
