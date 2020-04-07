# coding:utf-8

from flask import Flask, request

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    #类字典数据
    name = request.form.get("name")
    age = request.form.get("age")
    print("request data %s" % request.data)
    print("args %s" % request.args)
    print("request.url %s " % request.url)


    return "hello result name = %s age %s" % (name, age)

if __name__ == "__main__":
    app.run(debug=True)
