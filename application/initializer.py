class LoggerInstance(object):
    def __new__(cls):
        from application.main.utility.logger.custom_logging import LogHandler
        return LogHandler()


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.routers.health_checks import router as router_health_check
        from application.main.routers.hello_world import router as router_hello_world
        from application.main.routers.api_response import router as response_manager_test
        from application.main.routers.question_classifier import router as router_question_classification
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(router_health_check, prefix='/api/v1', tags=['Health'])
        router.include_router(router_hello_world, prefix='/api/v1', tags=['Hello World'])
        router.include_router(response_manager_test, prefix='/api/v1', tags=['Response Manager'])
        router.include_router(router_question_classification, prefix='/api/v1', tags=['Classification'])
        return router

class DataBaseInstance(object):
    def __new__(cls):
        from application.main.infrastructure.database import db
        return db.DataBase()


# instance creation
logger_instance = LoggerInstance()
db_instance = DataBaseInstance()