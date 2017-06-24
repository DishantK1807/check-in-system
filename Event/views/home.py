from flask import Flask, request, render_template
from flask_session import Session
from flask_mysqldb import MySQL

import hashlib
from codecs import encode

from Event.helpers import *
from Event import app
from Event import mysql

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if session['user_id'] == 0:
        return render_template('indexa.html')

    elif session['user_id'] == 1:
        return render_template('index.html')
