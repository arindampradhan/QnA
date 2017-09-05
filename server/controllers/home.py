# -*- coding: utf-8 -*-
from server import app
from flask import render_template, request


@app.route('/')
def start():
    return render_template('dashboard.html')


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/table')
def table():
    return render_template('table.html')
