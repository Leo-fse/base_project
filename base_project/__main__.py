import logging

from libs.test import main
from libs.utils.c_logger import convert_traceback_to_oneline

logger = logging.getLogger(__name__)
err_logger = logging.getLogger("errorLog")


def devide(a, b):
    try:
        print(f"result: { a / b } expression: resutl = {a} / {b}")
    except Exception as e:
        logger.error(e)
        err_logger.error(f"{e} a = {a}, b = {b}", exc_info=True)


if __name__ == "__main__":
    devide(1, 0)
    main(3, 5)
    main("uuu", 1)
