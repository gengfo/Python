from flask import Flask, redirect, session, url_for

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1> hello %s! </h1>'


@app.route('/login')
def login():
    session['logged_in']=True
    return redirect(url_for('hello'))

if __