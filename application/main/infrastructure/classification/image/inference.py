from tensorflow.keras.applications.imagenet_utils import decode_predictions
from application.initializer import LoggerInstance
from PIL import Image
import numpy as np
import tensorflow as tf
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
logger = LoggerInstance().get_logger(__name__)
classifier_model = None


class InferenceTask:

    @staticmethod
    async def load_model(classifier_model_name):
        if classifier_model_name == "MOBILENET_V2":
            model = tf.keras.applications.MobileNetV2(weights="imagenet")
        elif classifier_model_name == "INCEPTION_V3":
            model = tf.keras.applications.InceptionV3(weights="imagenet")
        else:
            model = tf.keras.applications.MobileNetV2(weights="imagenet")

        return model

    async def predict(self, classifier_model_name, image: Image.Image, shape):
        global classifier_model
        if classifier_model is None:
            classifier_model = await self.load_model(classifier_model_name)
        image = np.asarray(image.resize(shape))
        image = np.array(image)[..., :3] / 255.0
        image = np.expand_dims(image, 0)
        result = classifier_model.predict(image, 2)
        result = decode_predictions(
                result, top=5
        )[0]
        response = []
        for i, res in enumerate(result):
            resp = dict()
            resp["class"] = res[1]
            resp["confidence"] = f"{res[2] * 100:0.2f} %"
            response.append(resp)
        return response
