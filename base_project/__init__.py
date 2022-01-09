import logging
import logging.config
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "."))

from settings import LOG_CONFIG_PATH  # NOQA

logging.config.fileConfig(LOG_CONFIG_PATH, disable_existing_loggers=False)
