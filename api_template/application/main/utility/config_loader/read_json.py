import json
from abc import ABC
from pathlib import Path

from application.main.config import settings
from application.main.utility.config_loader.config_interface import ConfigReaderInterface
from application.main.utility.config_loader.serializer import Struct


class JsonConfigReader(ConfigReaderInterface, ABC):

    def __init__(self):
        super(JsonConfigReader, self).__init__()

    def read_config_from_file(self, config_filename: str):
        conf_path = Path(__file__).joinpath(settings.APP_CONFIG.SETTINGS_DIR, config_filename)
        with open(conf_path) as file:
            config = json.load(file)
        config_object = Struct(**config)
        return config_object
