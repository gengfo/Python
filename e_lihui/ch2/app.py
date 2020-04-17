# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, make_response


app = Flask(__name__)

@app.route('/say')
def hi():
    return  redirect(url_for('say_hello'))

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

# bind multiple URL for one view function
@app.route('/hi')
#@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'

# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('say_hello')))
    response.set_cookie('name',name)
    return  response

if __name__ == '__main__' :
	app.run(port=5000, debug=True)