import boto3, botocore

dynamodb = boto3.resource("dynamodb")


def get_images_table():
    """
    Method connects to Dynamo and gets the instance of existing "images" table in the specified enviormnet
    :return: instance of "images" table
    """
    return dynamodb.table("images")


def get_s3_resource():
    """
    Get S3 resource to store the images
    :return:
    """
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""
    return boto3.client("s3", AWS_ACCESS_KEY, AWS_SECRET_KEY)