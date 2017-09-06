# -*- coding: utf-8 -*-
from server import app
from server.helpers.tools import *
from flask import render_template, request, jsonify,make_response
from bson import ObjectId
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get('MONGODB_URL')
MONGODB_DB = os.environ.get('MONGODB_DATABASE')
DB = '{0}/{1}'.format(MONGODB_URL, MONGODB_DB)
client = MongoClient(DB)
db = client.devdb

limiter = Limiter(app, key_func=get_remote_address)

@limiter.limit('3 per day')
@app.route('/api/rate-limit')
def rate_limit():
    return jsonify({'checking': 'not crossed the rate limit'})

@app.route('/api/questions')
@validate_api
@limiter.limit('100 per day')
def questions():
    q = db.question.find({})
    qs = list(q)
    return bsonify(qs)


@app.route('/getuser')
@limiter.limit('100 per day')
@validate_api
def get_user():
    return jsonify({
        'user': session.get('username'),
        'api_key': session.get('api_key'),
        'request_count': session.get('request_count')
    })

@app.route('/api/answer/<question_id>')
@validate_api
@limiter.limit('100 per day')
def answer(question_id):
    ans = db.answer.find_one({'question_id': question_id})
    ans = bdict(ans)
    return jsonify(ans)

@app.route('/api/count')
@validate_api
@limiter.limit('100 per day')
def user_count():
    u_count = db.user.count()
    q_count = db.question.count()
    return jsonify({'user_count': u_count, 'question_count': q_count})