import logging
import logging.config

from settings import LOG_CONFIG_PATH
from some_module import some_module

logging.config.fileConfig(LOG_CONFIG_PATH, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

logger.debug({"action": "test", "status": "debug", "message": "start"})
logger.info({"action": "test", "status": "info", "message": "start"})
logger.warning({"action": "test", "status": "warning", "message": "start"})
