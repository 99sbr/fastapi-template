from typing import List
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from application.initializer import (db_instance, logger_instance)
from application.main.utility.manager.response_manager import SearchAnswerResponse


_db = db_instance
router = APIRouter(prefix='/response-manager')
logger = logger_instance.get_logger(__name__)


@router.get('/',response_model=List[SearchAnswerResponse])
async def response_manager_test():
    logger.info('Response Manager')
    data = {}
    return [data]
