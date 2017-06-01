from flask import render_template, Blueprint
from app import app
from app.models import *

mod_propriedade = Blueprint('propriedade', __name__, url_prefix='/propriedade')


@mod_propriedade.route('/')
def propriedade_index():
	return "propriedade index"