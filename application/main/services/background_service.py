from application.initializer import (db_instance, logger_instance)


class BackgroundService(object):

    def __init__(self):
        self.db = db_instance
        self.logger = logger_instance.get_logger(__name__)

    def run_some_task(self):
        self.logger.debug('Task Completed')
        self.db.insert_single_db_record({"Status": "Completed"})