from flask import Flask
from flask_session import Session
from flask_mysqldb import MySQL

from tempfile import gettempdir

app = Flask(__name__)

Flask.secret_key = '308ec91466f28042f2fcde5cf346fd5afd0af824'

app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = '456123'
app.config['MYSQL_DB']          = 'eventsapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.config['SECRET_KEY'] = '308ec91466f28042f2fcde5cf346fd5afd0af824'
# configure session to use filesystem (instead of signed cookies)
app.config['SESSION_FILE_DIR']  = gettempdir()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE']      = 'filesystem'
Session(app)

from Event.helpers import *
from Event.views import home
from Event.views import login
from Event.views import admin
from Event.views import user

if __name__ == '__main__':
    app.run(debug=True, SECRET_KEY='308ec91466f28042f2fcde5cf346fd5afd0af824')
