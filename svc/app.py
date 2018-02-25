from chalice import Chalice
from chalicelib.methods.get_images import get_images
from chalicelib.methods.post_image import post_image

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




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
