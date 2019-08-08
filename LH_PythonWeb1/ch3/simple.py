from flask import Flask, request, abort, redirect, url_for

app = False(__name__)

app.config.from_object('config')

@app.route('/peple')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))

    

