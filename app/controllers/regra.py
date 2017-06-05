from flask import render_template, Blueprint, session, abort, flash, redirect, url_for

mod_regra = Blueprint('regra', __name__, url_prefix='/regra', template_folder='templates')
# @TODO fazer metodos controlador regra
# @TODO fazer views regra

@mod_regra.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
    return render_template('regra/index.html')
