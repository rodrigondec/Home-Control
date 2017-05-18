from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

dados = {}

app.config.from_object('config')

# Add log handler
handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=100000, backupCount=50)
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error

from app.controllers import mod_propriedade as propriedade_module

app.register_blueprint(propriedade_module)