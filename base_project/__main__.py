import logging
import os
import traceback

from libs.utils.c_logger import convert_traceback_to_oneline

logger = logging.getLogger(__name__)
a, b = 1, 0
try:
    print(a / b)
except Exception as e:
    logger.error(f"{e}|{convert_traceback_to_oneline(traceback.format_exc())}")
