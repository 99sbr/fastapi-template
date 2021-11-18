import logging
import sys
from logging.handlers import TimedRotatingFileHandler, SocketHandler
from pathlib import Path
from application.main.config import settings
from application.main.utility.config_loader import ConfigReaderInstance


logging_config = ConfigReaderInstance.yaml.read_config_from_file(
    settings.LOG_CONFIG_FILENAME)


class Handlers:

    def __init__(self):
        self.formatter = logging.Formatter(logging_config.FORMATTER)
        self.log_filename = Path().joinpath(
            settings.APP_CONFIG.LOGS_DIR, logging_config.FILENAME)
        self.rotation = logging_config.ROTATION

    def get_console_handler(self):
        """

        :return:
        """
        console_handler = logging.StreamHandler(sys.stdout.flush())
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        """

        :return:
        """
        file_handler = TimedRotatingFileHandler(
            self.log_filename, when=self.rotation)
        file_handler.setFormatter(self.formatter)
        return file_handler

    def get_socket_handler(self):
        socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
        return socket_handler

    def get_handlers(self):
        return [self.get_console_handler(), self.get_file_handler(), self.get_socket_handler()]
