from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app.forms import LoginForm, ComponentForm, ClientForm
from app.models import *

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard', template_folder='templates')


# @TODO fazer view index


@mod_dashboard.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario is not None and usuario.senha == form.senha.data:
            flash('Usuario logado!')
            session['logged_in'] = True
            session['id_usuario'] = usuario.id_usuario
            return redirect(url_for('dashboard.index'))
        else:
            flash('Email ou senha incorretos. Tente novamente!')
            return render_template('dashboard/login.html', form=form)
    return render_template('dashboard/login.html', form=form)


@mod_dashboard.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')

@mod_dashboard.route('/')
def index():
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        client = Client.query.filter_by(id_client=1).first()
        modulo = client.component
        components = False
        if modulo.acessivel_por(usuario):
            components = modulo.components
        else:
            for modulo_i in Component.query.filter((Component.tipo=='modulo_privado')).all():
                if modulo_i.acessivel_por(usuario):
                    modulo = modulo_i
                    components = modulo.components
            if not components:
                return "Nenhum modulo privado com o usuário encontrado!"
        return render_template('dashboard/modulo.html', components=components, modulo=modulo, pai=modulo.achar_pai())
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')

@mod_dashboard.route('/modulo/<id_modulo>')
def modulo(id_modulo):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        modulo = Component.query.filter_by(id_component=id_modulo).first()
        if not modulo.acessivel_por(usuario):
            flash('Você não tem acesso à esse modulo!')
            return redirect('/dashboard/')
        components = modulo.components

        return render_template('dashboard/modulo.html', components=components, modulo=modulo, pai=modulo.achar_pai())
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dashboard.route('/leaf/<id_leaf>')
def leaf(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.acessivel_por(usuario):
            flash('Essa leaf não é liberada para você')
            return redirect('/dashboard/')
        dispositivos = Dispositivo.query.filter_by(leaf_id=id_leaf)
        return render_template('dashboard/leaf.html', dispositivos=dispositivos, leaf=leaf, pai=leaf.achar_pai())
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dashboard.route('/component/cadastrar/<id_component_pai>', methods=['GET', 'POST'])
def cadastrar_component(id_component_pai):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        component_pai = Component.query.filter_by(id_component=id_component_pai).first()
        if not component_pai.alteravel_por(usuario):
            flash('Você não tem permissão para alterar esse modulo')
            return redirect('/dashboard/')

        form = ComponentForm()
        if form.validate_on_submit():
            if form.tipo_component.data == 'Leaf':
                component = Leaf(form.nome.data)
            elif form.tipo_component.data == 'Modulo':
                component = Modulo(form.nome.data)
            else:
                component = ModuloPrivado(form.nome.data)

            component_pai = Component.query.filter_by(id_component=id_component_pai).first()
            if component_pai is None:
                flash('Erro no id do component escolhido')
                return redirect(url_for('dashboard.index'))

            component_pai.add_component(component)

            db.session.add(component)
            db.session.commit()
            flash('Cmponent criado com sucesso')

            return redirect(url_for('dashboard.index'))
        return render_template("dashboard/cadastrar_component.html", form=form)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dashboard.route('/propriedade/cadastrar', methods=['GET', 'POST'])
def cadastrar_propriedade():
    if 'logged_in' in session:
        print(session['id_usuario'])
        admin = Administrador.query.filter_by(id_usuario=session['id_usuario']).first()
        if admin is not None and admin.client is None:
            form = ClientForm()
            if form.validate_on_submit():
                admin.client = Client()
                admin.client.component = ModuloPrivado(form.nome.data)

                db.session.commit()

                flash('Propriedade cadastrada')
                return redirect(url_for('dashboard.index'))
            return render_template('dashboard/cadastrar_propriedade.html', form=form)
        else:
            flash('Você já tem uma propriedade ou não é administrador do sistema')
            return redirect('/dashboard/')
    else:
        flash('Entre primeiro')
        return redirect('/')
