from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import logger_instance
from application.main.services.question_classification_service import QuestionClassificationService

classification_service = QuestionClassificationService()
router = APIRouter()
logger = logger_instance.get_logger(__name__)


@router.get("/question-classify")
async def question_classification(input_text: str):
    logger.info('Question Classification')
    question_type = classification_service.classify(input_text)
    return question_type
