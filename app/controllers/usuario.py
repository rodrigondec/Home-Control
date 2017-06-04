from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import app
from app.models import *
from app.forms import UsuarioForm

mod_usuario = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')
# @TODO fazer metodos controlador usuario
# @TODO fazer views usuario

@mod_usuario.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
        return render_template('usuario/index.html')
    else:
        abort(403)

@mod_usuario.route('/criar')
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        # flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        # session['logged_in'] = True
        return redirect('/dashborad/')
    return render_template('cadastro.html', title='Sign In', form=form)
