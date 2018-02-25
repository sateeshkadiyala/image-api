import logging, os
from chalicelib.methods.helper import get_images_table, get_s3_resource, crop_image
from chalicelib.schemas.image_schema import ImageSchema
from chalice import Response
BUCKET = "S3_BUCKET"
AWS_KEY = "AWS_KEY"


def get_images(request):
    """
    :param request:
    :return: list of all images
    """

    result = get_images_table().scan()

    schema = ImageSchema()

    answer = schema.dump(result.get('Items', None), many=True)

    return Response(body=answer, headers={"Content-Type": "application/json"}, status_code=200)


def get_image_item(request, image_id):
    """

    :param request:
    :param image_id:
    :return:
    """

    result = get_images_table().get_item(Key=image_id)

    schema = ImageSchema()

    answer = schema.dump(result.get("Item", None), many=False)

    return Response(body=answer, headers={"Content-Type": "application/json"}, status_code=200)


def get_image_data(request, image_id):
    """

    :param request:
    :param image_id:
    :return:
    """
    try:
        path = '/temp/{}'.format(image_id)
        params = request.query_param_dict
        bbox = params['bbox']

        get_s3_resource.download_file(BUCKET, path)
        headers = {
            'Content-Type': "application/octet-stream",
            'Content-Length' : os.path.getsize(path)
        }
        if not bbox:
            f = open(path, 'rb')
        else:
            f = crop_image(open(path, 'rb'))

        return Response(body=f, headers=headers, status_code=200)

    except:
        raise Exception("Could not find image")