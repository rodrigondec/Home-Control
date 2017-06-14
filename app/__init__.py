from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import logging
from logging.handlers import RotatingFileHandler
import pymysql
from database import Session, init_db
from threading import Thread
from time import sleep

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add log handler
handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=100000, backupCount=50)
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Define the database object which is imported
# by modules and controllers

@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()

db_session = Session()

migrate = Migrate(app, db_session)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return redirect('/dashboard/login')

@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error

@app.errorhandler(403)
def not_authorized(error):
    app.logger.error(error)
    return error

from app.controllers.dashboard import mod_dashboard as dashboard_module
from app.controllers.dispositivo import mod_dispositivo as dispositivo_module
from app.controllers.monitor import mod_monitor as monitor_module
from app.controllers.usuario import mod_usuario as usuario_module

app.register_blueprint(dashboard_module)
app.register_blueprint(dispositivo_module)
app.register_blueprint(monitor_module)
app.register_blueprint(usuario_module)

init_db()

from app.models import Monitor

monitores =  db_session.query(Monitor).all()
for monitor in monitores:
    monitor.start()
