from bson.json_util import dumps
from flask import g, request, redirect, url_for, jsonify, session
from functools import wraps
import json

def bsonify(mongo_object):
    """Takes a single mongo object and converts them to jsonify"""
    json_string = dumps(mongo_object)
    json_dict = json.loads(json_string)
    return jsonify(json_dict)

def bdict(mongo_object):
    """Takes a single mongo object and converts them to dictionary"""
    json_string = dumps(mongo_object)
    json_dict = json.loads(json_string)
    return json_dict


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def validate_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return jsonify({'error': 'Invalid User', 'status': 503})
        return f(*args, **kwargs)
    return decorated_function
