from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from database import Session
from app.models import Administrador, Usuario, Component
from app.forms import UsuarioForm, AdicionarUsuariosForm

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
    db_session = Session()
    form = UsuarioForm()
    if form.validate_on_submit():
        if form.is_admin.data:
            usuario = Administrador(form.nome.data, form.email.data, form.senha.data)
        else:
            usuario = Usuario(form.nome.data, form.email.data, form.senha.data)
        db_session.add(usuario)
        db_session.commit()
        Session.remove()
        flash('Usuário criado com sucesso')

        return redirect('/')
    Session.remove()
    return render_template('usuario/cadastrar.html', title='Sign In', form=form)

@mod_usuario.route('/adicionar/<id_modulo>', methods=['GET', 'POST'])
def adicionar_usuario(id_modulo):
    if 'logged_in' in session:
        db_session = Session()
        usuario = db_session.query(Usuario).filter_by(id_usuario=session['id_usuario']).first()
        modulo = db_session.query(Component).filter_by(id_component=id_modulo).first()
        if not modulo.alteravel_por(usuario):
            flash('Você não tem permissão para alterar esse modulo')
            Session.remove()
            return redirect('/dashboard/')

        usuarios = db_session.query(Usuario).all()
        for user in modulo.usuarios:
            usuarios.remove(user)
        form = AdicionarUsuariosForm(usuarios)
        if form.validate_on_submit():
            for id_usuario in form.usuarios.data:
                user = db_session.query(Usuario).filter_by(id_usuario=id_usuario).first()
                modulo.add_usuario(user)
            db_session.commit()
            Session.remove()

            flash('Usuarios adicionados!')

            return redirect('/dashboard/modulo/'+id_modulo)
        Session.remove()
        return render_template('usuario/adicionar.html', form=form, modulo=modulo)
    else:
        flash('Entre primeiro')
        return redirect('/')
