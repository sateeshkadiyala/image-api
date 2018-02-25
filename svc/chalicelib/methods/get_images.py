import logging
from helper import get_images_table


def get_images(request):
    """
    :param request:
    :return: list of all images
    """

    result = get_images_table().scan()

    return result.get('Items', None)