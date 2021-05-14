from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import DataBaseInstance
from application.initializer import LoggerInstance

_db = DataBaseInstance()
router = APIRouter(prefix='/health-check')
logger = LoggerInstance().get_logger(__name__)


@router.get('/')
async def health_check():
    logger.info('Health Check⛑')
    _db.insert_single_db_record({"Status": "OK"})
    return JSONResponse(content='OK⛑', status_code=200)
