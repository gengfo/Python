# coding:utf-8

from flask import Flask, current_app

app = Flask(__name__)


# 1. 使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用配置类
class Config(object):
    DEBUG = True


# app.config.from_object(Config)

# 3.直接操作config的字典对象
app.config["DEBUG"] = True


@app.route("/")
def index():
    # a = 1/0
    # 读取app配置参数1
    # print(app.config.get("DEBUG"))

    # 读取app配置参数2
    print(current_app.config.get("DEBUG"))

    return "hello flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
