from chalice import Chalice
from chalicelib.methods.get_images import get_images, get_image_item
from chalicelib.methods.post_image import post_image, put_image_item

app = Chalice(app_name='image-api')


@app.route('/v1/image', methods=["GET", "POST"], content_types=['application/octet-stream'])
def images():
    """
    Routing logic for images retrieval and post
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting Images")
        return get_images(request)
    if request.method == "POST":
        app.log.debug("Upload image")
        return post_image(request)


@app.route('/v1/image/{id}', methods=["GET", "PUT"])
def image_metadata(image_id):
    """
    Routing logic for images  retrieval and post
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting Images")
        return get_image_item(request, image_id)
    if request.method == "PUT":
        app.log.debug("Upload image")
        return put_image_item(request, image_id)


@app.route('/v1/image/{id}/data', methods=["GET"])
def image_data(image_id):
    """
    Routing logic for images  retrieval and post
    :return:
    """
    request = app.current_request

    if request.method == "GET":
        app.log.debug("Getting Images")
        return get_image_item(request, image_id)



