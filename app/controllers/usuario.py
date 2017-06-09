from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import db
from app.models import Administrador, Usuario
from app.forms import UsuarioForm

mod_usuario = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates')

@mod_usuario.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
        return render_template('usuario/index.html')
    else:
        flash('Entre primeiro')
        return redirect('/')

@mod_usuario.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        if form.is_admin.data:
            usuario = Administrador(form.nome.data, form.email.data, form.senha.data)
        else:
            usuario = Usuario(form.nome.data, form.email.data, form.senha.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuário criado com sucesso')

        return redirect('/')
    return render_template('usuario/cadastrar.html', title='Sign In', form=form)

@mod_usuario.route('/adicionar/<id_modulo>', methods=['GET', 'POST'])
def adicionar_usuario(id_modulo):
    if 'logged_in' in session:
        print(session['logged_in'])
        return render_template('usuario/adicionar.html')
    else:
        flash('Entre primeiro')
        return redirect('/')
