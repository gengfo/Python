# encoding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机号码已注册'
        else:
            if password1 != password2:
                return u'两次密码不匹配'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
