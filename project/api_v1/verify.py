# coding:utf-8

from . import api
from flask import make_response
from project.utils.randchars import generate_chars
from captcha.image import ImageCaptcha


@api.route("/verify/image/<image_id>")
def verify(image_id):
    """
    get sign up verify image
    :param image_id: id of the verify image
    :return: verify image
    """

    # generate text and image
    text = generate_chars()
    image = ImageCaptcha()
    data = image.generate(text)

    response = make_response(data.getvalue())
    data.close()
    response.headers["Content-Type"] = "image/jpg"

    return response
