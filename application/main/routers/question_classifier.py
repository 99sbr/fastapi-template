from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance
from application.main.services.question_classification_service import QuestionClassificationService

router = APIRouter(prefix='/question-classify')
logger = LoggerInstance().get_logger(__name__)


@router.get("/")
async def question_classification(input_text: str):
    logger.info('Question Classification')
    question_type = QuestionClassificationService().classify(input_text)
    return question_type

