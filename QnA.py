#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from server import app
from flask import send_from_directory

if __name__ == '__main__':
    app.run(debug=True)
