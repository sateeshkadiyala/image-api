import logging
from chalicelib.methods.helper import get_images_table
from chalicelib.schemas.image_schema import ImageSchema


def get_images(request):
    """
    :param request:
    :return: list of all images
    """

    result = get_images_table().scan()

    schema = ImageSchema()

    answer = schema.dump(result.get('Items', None), many=True)

    return answer


def get_image_item(request, image_id):
    """

    :param request:
    :param image_id:
    :return:
    """

    result = get_images_table().get_item(Key=image_id)

    schema = ImageSchema()

    answer = schema.dump(result.get("Item", None), many=False)

    return answer
