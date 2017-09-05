# -*- coding: utf-8 -*-
from server import app
from server.helpers.tools import *
from flask import render_template, request, jsonify
from bson import ObjectId
from pymongo import MongoClient
import os

MONGODB_URL = os.environ.get('MONGODB_URL')
MONGODB_DB = os.environ.get('MONGODB_DATABASE')
DB = '{0}/{1}'.format(MONGODB_URL, MONGODB_DB)
client = MongoClient(DB)
db = client.devdb

@app.route('/api/questions')
@validate_api
def questions():
    q = db.question.find({})
    qs = list(q)
    return bsonify(qs)


@app.route('/api/answer/<question_id>')
@validate_api
def answer(question_id):
    ans = db.answer.find_one({'question_id': question_id})
    ans = bdict(ans)
    return jsonify(ans)

@app.route('/api/count')
@validate_api
def user_count():
    u_count = db.user.count()
    q_count = db.question.count()
    return jsonify({'user_count': u_count, 'question_count': q_count})