import logging

from libs.janken import JankenSimulator

logger = logging.getLogger(__name__)
e_logger = logging.getLogger("errorLog")


if __name__ == "__main__":
    janken = JankenSimulator()
    janken.simulate()
