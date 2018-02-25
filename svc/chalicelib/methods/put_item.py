from chalicelib.methods.helper import get_images_table
from chalicelib.schemas.image_schema import ImageSchema
from marshmallow import ValidationError
from chalicelib.methods.post_image import build_metadata
from chalice import BadRequestError


def put_images_item(metadata):
    """
    saves the metadata to the dynamo table "images"
    :param metadata:
    :return:
    """

    try:
        image_schema = ImageSchema()

        item = image_schema.load(metadata)

        get_images_table().put_item(Item = item)

    except ValidationError:
        pass


def put_image_item(request, image_id):
    """

    :param request:
    :param image_id:
    :return:
    """
    result = get_images_table().get_item(Key=image_id)

    if not result:
        raise BadRequestError("Item not found")

    metadata = build_metadata(request.raw_body)

    get_images_table().update_item(Key=image_id, item=metadata)



