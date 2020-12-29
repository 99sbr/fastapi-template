import logging
from typing import List

from application.main.utility.logger.handlers import Handlers


class LogHandler(object):

    def __init__(self):
        self.available_handlers: List = Handlers().get_handlers()

    def get_logger(self, logger_name):
        """

        :param logger_name:
        :return:
        """
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        if logger.hasHandlers():
            logger.handlers.clear()
        for handler in self.available_handlers:
            logger.addHandler(handler)
        logger.propagate = False
        return logger
