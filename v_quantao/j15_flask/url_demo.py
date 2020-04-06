# coding:utf-8

from flask import Flask, current_app

app = Flask(__name__)


@app.route("/")
def index():
    return "hello flask"


@app.route("/post_only", methods=["POST"])
def post_only():
    return "post only"


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
