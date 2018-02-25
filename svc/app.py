from chalice import Chalice
from chalicelib.methods.get_images import get_images, get_image_item
from chalicelib.methods.post_image import put_images_item, post_image

app = Chalice(app_name='image-api')


@app.route('/v1/image', methods=["GET", "POST"], content_types=['application/octet-stream'])
def images():
    """
    Routing logic for images retrieval and post
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting All Images Metadata")
        return get_images(request)
    if request.method == "POST":
        app.log.debug("Upload an image")
        return post_image(request)


@app.route('/v1/image/{id}', methods=["GET", "PUT"])
def image_metadata(image_id):
    """
    Routing logic for images  retrieval and post
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting an Image metadata")
        return get_image_item(request, image_id)
    if request.method == "PUT":
        app.log.debug("Update image metadata")
        return put_images_item(request, image_id)


@app.route('/v1/image/{id}/data', methods=["GET"])
def image_data(image_id):
    """
    Routing logic for image data with or without bbox
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting Image data with optional parameters of bounding box")
        return get_image_item(request, image_id)



