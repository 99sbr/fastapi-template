from application.initializer import (db_instance, logger_instance)


class BackgroundService(object):

    def __init__(self):
        self.db = db_instance
        self.logger = logger_instance

    def run_some_task(self):
        self.logger.info('Task Completed')
        self.db.insert_single_db_record({"Status": "Completed"})