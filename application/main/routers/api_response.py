from typing import List
from typing import Optional

from fastapi.routing import APIRouter
from pydantic import BaseModel

from application.initializer import (db_instance, logger_instance)


class SearchAnswerResponse(BaseModel):
    key1: Optional[float] = None
    key2: Optional[str] = None
    key3: Optional[int] = None


_db = db_instance
router = APIRouter(prefix='/response-manager')
logger = logger_instance.get_logger(__name__)


@router.get('/', response_model=List[SearchAnswerResponse])
async def response_manager_test():
    logger.info('Response Manager')
    data = {}
    return [data]
