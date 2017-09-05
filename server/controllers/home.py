# -*- coding: utf-8 -*-
from server import app
from flask import render_template, request, send_from_directory

@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/table')
def table():
    return render_template('table.html')


# dynamic routing for client js files
# for production choose nginx
@app.route("/public/<path:path>")
def public_path(path):
    return send_from_directory(app.CLIENT_DIR, path)
