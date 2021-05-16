import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from application.main.config import settings
from application.main.utility.config_loader import ConfigReaderInstance


logging_config = ConfigReaderInstance.yaml.read_config_from_file(
    settings.LOG_CONFIG_FILENAME)

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Handlers:

    def __init__(self):
        self.formatter = CustomFormatter()
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

    def get_handlers(self):
        return [self.get_console_handler(), self.get_file_handler()]