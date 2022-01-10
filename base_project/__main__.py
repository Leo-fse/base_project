import logging

from libs.janken import janken

logger = logging.getLogger(__name__)
e_logger = logging.getLogger("errorLog")


if __name__ == "__main__":
    janken.main()
