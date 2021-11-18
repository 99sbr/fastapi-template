from PIL import Image
from io import BytesIO
import numpy as np
import boto3


class S3ImageUtility:

    @classmethod
    def read_image_from_s3(cls, bucket, key, region_name='ap-southeast-1'):
        """Load image file from s3.

        Parameters
        ----------
        bucket: string
            Bucket name
        key : string
            Path in s3

        Returns
        -------
        np array
            Image array
        """
        s3 = boto3.resource('s3', region_name='ap-southeast-1')
        bucket = s3.Bucket(bucket)
        object = bucket.Object(key)
        response = object.get()
        file_stream = response['Body']
        im = Image.open(file_stream)
        return np.array(im)

    @classmethod
    def write_image_to_s3(cls, img_array, bucket, key, region_name='ap-southeast-1'):
        """Write an image array into S3 bucket

        Parameters
        ----------
        bucket: string
            Bucket name
        key : string
            Path in s3

        Returns
        -------
        None
        """
        s3 = boto3.resource('s3', region_name)
        bucket = s3.Bucket(bucket)
        object = bucket.Object(key)
        file_stream = BytesIO()
        im = Image.fromarray(img_array)
        im.save(file_stream, format='jpeg')
        object.put(Body=file_stream.getvalue())

