from typing import List

from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import DataBaseInstance
from application.initializer import LoggerInstance
from application.main.utility.manager.response_manager import *


_db = DataBaseInstance()
router = APIRouter(prefix='/response-manager')
logger = LoggerInstance().get_logger(__name__)


@router.get('/',response_model=List[SearchAnswerResponse])
async def response_manager_test():
    logger.info('Response Manager')
    data = {}
    return [data]
