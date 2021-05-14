from abc import ABC
from typing import Dict

import motor.motor_asyncio

from application.main.config import settings
from application.main.infrastructure.database.db_interface import DataBaseOperations
from application.main.utility.config_loader import ConfigReaderInstance


class Mongodb(DataBaseOperations, ABC):

    def __int__(self):
        super(Mongodb, self).__init__()
        self.db_config = ConfigReaderInstance.yaml.read_config_from_file(
            settings.DB + '_config.yaml')

    async def fetch_single_db_record(self, unique_id: str):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)
        collection = client[self.db_config.collection]

    async def update_single_db_record(self, record: Dict):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)

    async def update_multiple_db_record(self, record: Dict):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)

    async def fetch_multiple_db_record(self, unique_id: str):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)

    async def insert_single_db_record(self, record: Dict):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)
        collection = client[self.db_config.collection]
        document = record
        return await collection.insert_one(document)

    async def insert_multiple_db_record(self, record: Dict):
        connection_uri = 'mongodb://' + \
            str(self.db_config.test.host) + str(self.db_config.test.port)
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)
