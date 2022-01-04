import time
import logging


def get_logger(name="pst logger"):
    """
    Returns logging.logger with specific datetime formatting

    :param name: name of logger
    :return: logging.logger
    """

    logger = logging.getLogger(name)
    logging.basicConfig(format="%(asctime)s > %(message)s", level=logging.DEBUG)
    logger.setLevel(1)
    return logger


def get_timestamp():
    """Convenience method to create a pretty timestamp"""
    return time.strftime("%Y-%b-%d_%H:%M:%S")
