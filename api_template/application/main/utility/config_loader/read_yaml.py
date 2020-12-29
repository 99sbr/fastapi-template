from pathlib import Path

import yaml

from application.main.config import settings
from application.main.utility.config_loader.config_interface import ConfigReaderInterface
from application.main.utility.config_loader.serializer import Struct


class YamlConfigReader(ConfigReaderInterface):

    def __init__(self):
        super(YamlConfigReader, self).__init__()

    def read_config_from_file(self, config_filename: str):
        conf_path = Path(__file__).joinpath(settings.APP_CONFIG.SETTINGS_DIR, config_filename)
        with open(conf_path) as file:
            config = yaml.safe_load(file)
        config_object = Struct(**config)
        return config_object
