from flask import Flask, render_template, url_for, request, session, redirect
import os
from server import app
from pymongo import MongoClient
from flask import jsonify
import uuid

MONGODB_URL = os.environ.get('MONGODB_URL')
MONGODB_DB = os.environ.get('MONGODB_DATABASE')
DB = '{0}/{1}'.format(MONGODB_URL, MONGODB_DB)
client = MongoClient(DB)
db = client.devdb

@app.route('/')
def index():
    """route to dashboard if logged in else login page."""
    if not MONGODB_URL:
        return jsonify({'error': 'please add an environment file .env in root of project and restart your server.'})
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    """login post and get method to validate user"""
    if request.method == 'GET':
        return render_template('login.html')

    users = db.user
    login_user = users.find_one({'name': request.form['username']})
    api_key = ''
    try:
        tenent = db.tenent.find_one({'name': request.form['username']})
        if tenent:
            api_key = tenent['api_key']
    except:
        pass
    if login_user:
        session['user_id'] = str(login_user.get('_id'))
        session['username'] = request.form['username']
        session['api_key'] = api_key
        return redirect(url_for('index'))
    return render_template('message.html', message='Invalid username', status='503')

@app.route('/message')
def message():
    """Default message for user for false response or edge cases."""
    return render_template('message.html', message= 'Page not Found', status ='404')

@app.route('/logout')
def logout():
    """Logout as user"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register as user, create api_key add to sessions"""
    if session.get('username'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        existing_user = db.user.find_one({'name': request.form['username']})

        if existing_user is None:
            api_key = str(uuid.uuid4())
            username = request.form['username']
            user_id = db.user.insert({'name': username})
            db.tenent.insert({'name': username, 'api_key': api_key})
            session['user_id'] = str(user_id)
            session['username'] = request.form['username']
            session['api_key'] = api_key
            return redirect(url_for('index'))

        return render_template('message.html', status='409', message='That username already exists!')

    return render_template('register.html')
