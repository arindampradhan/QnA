# -*- coding: utf-8 -*-
from server import app
from dotenv import load_dotenv
import os
from os import path


# Directory
ROOT_DIR = path.dirname(path.dirname(__file__))
print(ROOT_DIR)
CLIENT_DIR = path.join(ROOT_DIR, 'public')
TEMPLATES_DIR = path.join(ROOT_DIR,'views')


# Environment Variables
load_dotenv(os.path.join(ROOT_DIR, ".env"))


# app config
app.config['SECRET_KEY'] = 'areallyrandomnumber'
app.debug = True
app.ROOT_DIR = ROOT_DIR
app.CLIENT_DIR = CLIENT_DIR
app.template_folder = TEMPLATES_DIR

# print(os.environ.get('MONGODB_DATABASE'))
# print(os.environ.get('MONGODB_URL'))
# app.config['MONGODB_SETTINGS'] = {
#     'db': os.environ.get('MONGODB_DATABASE'),
#     'host': os.environ.get('MONGODB_URL')
# }