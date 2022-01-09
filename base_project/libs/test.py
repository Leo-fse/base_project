import logging

logger = logging.getLogger(__name__)
err_logger = logging.getLogger("errorLog")


class TempClass:
    def add(self, a, b):
        logger.debug("start")
        try:
            logger.debug(f"result = {a + b}, a = {a}, b = {b}")
            return a + b
        except Exception as e:
            logger.error(e)
            err_logger.error(f"{e}, a = {a}, b = {b}", exc_info=True)
        finally:
            logger.debug("end")


def main(a, b):
    t = TempClass()
    t.add(a, b)
