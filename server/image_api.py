from flask import Blueprint, request

image_api = Blueprint("image_api", __name__)


@image_api.route("/click", methods=["POST"])
def click():
    print(request.json)
    return "YOYOYO", 200
