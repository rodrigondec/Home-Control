from flask import render_template, Blueprint, session, abort, flash, redirect, url_for

mod_dispositivo = Blueprint('dispositivo', __name__, url_prefix='/dispositivo', template_folder='templates')
# @TODO fazer metodos controlador dispositivo
# @TODO fazer views dispositivo

@mod_dispositivo.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
    return render_template('dispositivo/index.html')