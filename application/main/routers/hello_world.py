from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance

router = APIRouter()
logger = LoggerInstance().get_logger(__name__)


@router.get("/")
async def hello_world():
    logger.info('Hello World👍🏻')
    return JSONResponse(content={"message": "Hello World! 👍🏻"}, status_code=200)
