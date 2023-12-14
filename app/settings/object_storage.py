import os
from botocore.exceptions import ClientError
import boto3
import logging

from app.settings import get_settings
from app.settings.progress_percentage import ProgressPercentage
from fastapi import BackgroundTasks, File, UploadFile

FILE_DESTINATION = "app/static/images"

logger = logging.getLogger(__name__)

s3 = boto3.client(
    service_name            = "s3", 
    aws_access_key_id       = get_settings().OBJECT_STORAGE_ACCESS_KEY,
    aws_secret_access_key   = get_settings().OBJECT_STORAGE_SECRET_KEY,
    region_name             = get_settings().OBJECT_STORAGE_REGION,
    endpoint_url            = f"https://{get_settings().OBJECT_STORAGE_ENDPOINT_PUBLIC}"
)
    
def upload_file_to_bucket(file_obj, bucket = "audio", folder = "messages", object_name=None):
    if object_name is None:
        object_name = FILE_DESTINATION
    # Upload the file
    try:
        response = s3.put_object(
            Bucket=bucket,
            Key=f"{folder}/{object_name}", 
            Body=file_obj
        )

        response['public_url'] = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': f"{bucket}",
                'Key': f"{folder}/{object_name}"
            }
        )
        return response
    except ClientError as e:
        logging.error(e)
        return False

def download_file_from_bucket(bucket = "audio", folder = "messages", object_name=None):
    try:
        file = s3.Object(bucket, f"{folder}/{object_name}").get()['Body'].read()
        return response
    except ClientError as e:
        logging.error(e)
        return False
