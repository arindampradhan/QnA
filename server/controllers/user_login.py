from flask import Flask, render_template, url_for, request, session, redirect
import os
from server import app
from pymongo import MongoClient
from flask import jsonify

MONGODB_URL = os.environ.get('MONGODB_URL')
MONGODB_DB = os.environ.get('MONGODB_DATABASE')
DB = '{0}/{1}'.format(MONGODB_URL, MONGODB_DB)
client = MongoClient(DB)
db = client.devdb

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    users = db.user
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('message.html', message='Invalid username', status='503')

@app.route('/message')
def message():
    return render_template('message.html', message= 'Page not Found', status ='404')

@app.route('/getuser')
def get_user():
    return jsonify({'user': session['username']})

@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = db.user.find_one({'name': request.form['username']})

        if existing_user is None:
            db.user.insert({'name': request.form['username']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return render_template('message.html', status='409', message='That username already exists!')

    return render_template('register.html')
