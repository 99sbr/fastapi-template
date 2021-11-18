import os
from io import BytesIO
from PIL import Image
from application.main.config import settings


class BasicImageUtils:

    @classmethod
    async def read_image_file(cls, file, filename, cache=True) -> Image.Image:
        image = Image.open(BytesIO(file))
        if cache:
            image.save(os.path.join(settings.APP_CONFIG.CACHE_DIR, filename))
        return image
