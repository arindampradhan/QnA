# -*- coding: utf-8 -*-
from mongoengine import *

class User(Document):
    """User of q and a"""
    name = StringField(required=True, max_length=200)

class Question(Document):
    """Question by a user"""
    title = StringField(required=True, max_length=1000)
    private = BooleanField(required=False, default=False)
    user_id = StringField(required=True)

class Answer(Document):
    """Answer to a question"""
    body = StringField(max_length=10000)
    question_id = StringField(required=True)

class Tenent(Document):
    """Api request key and name"""
    api_key = StringField()
    name = StringField(max_length=200)