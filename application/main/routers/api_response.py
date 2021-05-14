from typing import List
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from application.initializer import (db_instance, logger_instance)
from typing import Optional
from pydantic import BaseModel



class SearchAnswerResponse(BaseModel):
	key1: Optional[float] = None
	key2: Optional[str] = None
	key3: Optional[int] = None

_db = db_instance
router = APIRouter(prefix='/response-manager')
logger = logger_instance.get_logger(__name__)


@router.get('/',response_model=List[SearchAnswerResponse])
async def response_manager_test():
    logger.info('Response Manager')
    data = {}
    return [data]
