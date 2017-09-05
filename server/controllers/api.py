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
def questions():
    q = db.question.find({})
    qs = list(q)
    return bsonify(qs)


@app.route('/api/answer/<question_id>')
def answer(question_id):
    ans = db.answer.find_one({'question_id': question_id})
    ans = bdict(ans)
    return jsonify(ans)


# Count number of users and questions
@app.route('/api/questions/count')
def question_count():
    count = db.question.count()
    return jsonify({'questions': count})

@app.route('/api/users/count')
def user_count():
    count = db.user.count()
    return jsonify({'users': count})