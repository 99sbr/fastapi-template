from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from application.initializer import logger_instance
from application.main.services.background_service import BackgroundService


router = APIRouter()
logger = logger_instance.get_logger(__name__)


@router.get('/task')
async def index_elastic_search(background_tasks: BackgroundTasks):
    logger.info("Request to run some task in background")
    background_tasks.add_task(func=BackgroundService().run_some_task, )
    return JSONResponse(content="Task Running in Background", status_code=200)