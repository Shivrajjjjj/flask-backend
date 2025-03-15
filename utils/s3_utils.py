import boto3
from flask import current_app

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        region_name=current_app.config["AWS_REGION"],
    )

def upload_to_s3(file, file_name):
    s3 = get_s3_client()
    try:
        s3.upload_fileobj(file, current_app.config["AWS_S3_BUCKET_NAME"], file_name)
        return True
    except Exception as e:
        print(f"S3 Upload error: {e}")
        return False

def get_user_images_from_s3(user_id):
    #get all the image names from the database, and then create the presigned urls.
    return []