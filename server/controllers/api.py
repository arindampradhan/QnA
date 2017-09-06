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
    return jsonify({'checking': 'not crossed the rate limit', 'test limit': 3})

@app.route('/api/questions')
# @validate_api
@limiter.limit('100 per day')
def questions():
    """Aggregate question and answer"""
    q = db.question.aggregate([{
        '$lookup': {
            'from': 'answer',
            'localField': '_id',
            'foreignField': 'question_id',
            'as': 'answers'
        }}])

    # private filter
    qs = list(q)
    user_id = session.get('user_id')
    q2 = []
    for qsn in qs:
        if qsn.get('user_id') == user_id and qsn.get('private') is True:
           q2.append(qsn)
        elif qsn.get('private') is False:
            q2.append(qsn)
        else:
            pass
    return bsonify(q2)


@app.route('/getuser')
@limiter.limit('100 per day')
def get_user():
    """Inital user data."""
    return jsonify({
        'username': session.get('username'),
        'api_key': session.get('api_key'),
        'request_count': session.get('request_count'),
        'user_id': session.get('user_id'),
        'rate limit': '100 per day'
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