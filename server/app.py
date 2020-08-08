from flask import Flask, g
from server.image_api import image_api

app = Flask(__name__)
app.register_blueprint(image_api, url_prefix="/image")


@app.route("/")
def hello():
    return "HELLO", 200


@app.after_request
def do_something_whenever_a_request_has_been_handled(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, PUT, GET, OPTIONS")
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)

