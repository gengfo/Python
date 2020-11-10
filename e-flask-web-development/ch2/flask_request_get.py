from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/hello1', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name', 'Flask')
    return '<h1> hello %s!</h1>' % name + url_for('hello')


if __name__ == '__main__':
    app.run(debug=True)
