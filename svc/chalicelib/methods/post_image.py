from chalicelib.methods.helper import get_s3_resource
import uuid

BUCKET = "S3_BUCKET"


def post_image(request):
    """
    post image
    :param request:
    :return:
    """
    body = request.raw_body

    file_name = uuid.uuid4()

    temp_file = '/temp/' + file_name

    with open(temp_file, 'wb') as file:
        file.write(body)

    return upload_file_to_s3(temp_file, file_name)


def upload_file_to_s3(file, file_name):
    """
    Method that actually uploads image to s3 bucket
    :param file:
    :return:
    """
    try:

        s3 = get_s3_resource()

        s3.upload_file(
            file,
            BUCKET
        )

        post_images_item(file_name)

    except Exception:
        raise Exception("Unable to upload image")