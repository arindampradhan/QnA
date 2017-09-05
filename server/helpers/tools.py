from bson.json_util import dumps
from flask import jsonify
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
