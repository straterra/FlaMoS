#!/usr/bin/env python3

# Written by Thomas York

# Imports
from flask import Flask
from flask_hashing import Hashing
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_reverse_proxy import FlaskReverseProxied
from flask_socketio import SocketIO

# Flask Setup
app = Flask(__name__)
app.config.from_object(Config)
hashing = Hashing(app)
db = SQLAlchemy(app)
proxied = FlaskReverseProxied(app)
socketio = SocketIO(app, logger=False, threaded=True)

# Route setup
from app.routes import *
