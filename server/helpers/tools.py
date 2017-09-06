from bson.json_util import dumps
from flask import g, request, redirect, url_for, jsonify, session, make_response
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
    """to check if user is logged in."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def validate_api(f):
    """Validate apis for different cases."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if str(request.headers.get('api_key')) != str(session.get('api_key')):
            # print(request.headers.get('api_key'))
            # print(session.get('api_key'))
            return make_response(jsonify({'error': 'Invalid api_key', 'status': 400}), 400)
        request_count = session.get('request_count')
        if request_count is None:
            session['request_count'] = 0
        else:
            session['request_count'] += 1
        if session.get('username') is None:
            return make_response(jsonify({'error': 'Invalid User', 'status': 503}), 503)
        return f(*args, **kwargs)
    return decorated_function
