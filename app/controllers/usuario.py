from flask import render_template, Blueprint
from app import app
from app.models import *

mod_usuario = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates/usuario')


@mod_usuario.route('/')
def usuario_index():
    if 'logged_in' in session:
        print(session['logged_in'])
        return 'dados'
    else:
        abort(403)

