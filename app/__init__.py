from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import logging
from logging.handlers import RotatingFileHandler
import pymysql
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
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error

from app.controllers.dashboard import mod_dashboard as dashboard_module
from app.controllers.propriedade import mod_propriedade as propriedade_module
from app.controllers.usuario import mod_usuario as usuario_module
from app.controllers.login import mod_login as login_module

app.register_blueprint(dashboard_module)
app.register_blueprint(propriedade_module)
app.register_blueprint(usuario_module)
app.register_blueprint(login_module)

db.create_all()