import logging

from settings import ROOT_DIR

logger = logging.getLogger(__name__)


def convert_traceback_to_oneline(tb):
    return tb.rstrip("\n").replace("\n", "|")
