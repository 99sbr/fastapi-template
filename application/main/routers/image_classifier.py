from fastapi import File, UploadFile
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance
from application.main.services.image_classification_service import ImageClassificationService
from application.main.utility.manager.image_utils import BasicImageUtils

image_classification_service = ImageClassificationService()
router = APIRouter(prefix='/image-classify')
logger = LoggerInstance().get_logger(__name__)


@router.post("/")
async def image_classification(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    logger.info('Image Classification')
    image = await BasicImageUtils.read_image_file(await file.read(), filename=file.filename, cache=True)
    image_category = await image_classification_service.classify(image)
    return image_category
