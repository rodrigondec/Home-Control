from flask import render_template, Blueprint
from app import app
from app.models import *

mod_usuario = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')


@mod_usuario.route('/')
def usuario_index():
	return "usuario index"