import abc
from typing import Dict


class DataBaseOperations(abc.ABC):

    def __init__(self):
        super().__init__()

    def update_single_db_record(self, record: Dict):
        raise NotImplementedError()

    def update_multiple_db_record(self, record: Dict):
        raise NotImplementedError()

    def fetch_single_db_record(self, unique_id: str):
        raise NotImplementedError()

    def fetch_multiple_db_record(self, unique_id: str):
        raise NotImplementedError()

    def insert_single_db_record(self, record: Dict):
        raise NotImplementedError()

    def insert_multiple_db_record(self, record: Dict):
        raise NotImplementedError()
