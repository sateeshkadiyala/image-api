from chalicelib.methods.helper import get_s3_resource
from chalicelib.methods.put_item import put_images_item
import uuid, datetime
from collections import defaultdict
from chalice import ChaliceViewError


BUCKET = "S3_BUCKET"


def post_image(request):
    """
    post image
    :param request:
    :return:
    """
    body = request.raw_body

    metadata = build_metadata(body)

    metadata["file_name"] = uuid.uuid4()

    temp_file = '/temp/' + metadata["file_name"]

    with open(temp_file, 'wb') as file:
        file.write(body)

    return upload_file_to_s3(temp_file, metadata)


def upload_file_to_s3(file, metadata):
    """
    Method that actually uploads image to s3 bucket
    :param file:
    :return:
    """
    try:

        s3 = get_s3_resource()

        s3.upload_file(
            file,
            BUCKET,
            metadata['file_name']
        )
        metadata["url"] = BUCKET + metadata["file_name"]

        # write metadata to the dynamodb table instance
        put_images_item(metadata)

    except Exception:
        raise ChaliceViewError("Unable to upload image")


def build_metadata(body):
    """
    Build metadata from the post body form
    :param body:
    :return:
    """
    metadata = defaultdict(str)
    try:
        metadata["file_name"] = body["file_name"]
        metadata["dimensions"] = [int(body["width"]), int(body["height"])]
        metadata["type"] = body["type"]
        metadata["uploaded_at"] = datetime.datetime.now()
        return metadata
    except KeyError:
        raise Exception("Error building metadata for the give file.")