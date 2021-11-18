from application.main.config import settings
from application.initializer import LoggerInstance
from application.main.infrastructure.classification.image.inference import InferenceTask


class ImageClassificationService(object):

    def __init__(self):
        self.logger = LoggerInstance().get_logger(__name__)
        self.image_model = InferenceTask()
        self.image_classification_model = settings.MOBILENET_V2
        self.IMAGE_SHAPE = (224, 224)

    async def classify(self, image_file):
        self.logger.info(f'Model IN use : {self.image_classification_model}')
        label = await self.image_model.predict(classifier_model_name=self.image_classification_model, image=image_file,
                                               shape=self.IMAGE_SHAPE)
        return label
