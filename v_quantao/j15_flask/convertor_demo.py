# coding:utf-8

from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 127.0.0.1:5000/goods/123
# 默认字符串
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return "goods detail page %s" % goods_id


# 1. 定义装换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask 会使用这个属性来进路由的正则匹配
        self.regex = regex


# 2. 将自定义的转换器添加到flask应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter

# class MobileConverter(BaseConverter):
#     def __init__(self,url_map):
#         super(MobileConverter,self).__init__(url_map)
#         self.regex = r'1[345678]\d{9}'

class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter,self).__init__(url_map)
        self.regex = r'1[345678]\d{9}'

    def to_python(self, value):
        return value

    def to_url(self,value):
        pass
    


# 127.0.0.1:5000/send/1234
#@app.route("/send/<re(r'1[345678]\d{9}'):mobile>")
#def send_msg(mobile):
#    return "send msg to %s" % mobile

# @app.route("/send/<mobile:mobile_num>")
# def send_msg(mobile_num):
#     return "send msg to %s" % mobile_num

@app.route("/send/<mobile:mobile_num>")
def send_msg():
    pass

@app.route("/send/<mobile:mobile_num>")
def call():
    pass



if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
