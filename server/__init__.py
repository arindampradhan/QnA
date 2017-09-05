# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
app = Flask('server')
from server.controllers import *
from server.config import *



