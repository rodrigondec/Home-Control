from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import db
from app.models import *
from app.forms import ClientForm

mod_component = Blueprint('component', __name__, url_prefix='/component', template_folder='templates')
# @TODO fazer metodos controlador component
# @TODO fazer views component

@mod_component.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
    return render_template('component/index.html')


@mod_component.route('/propriedade/cadastrar', methods=['GET', 'POST'])
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
                return redirect(url_for('component.index'))
            return render_template('component/cadastrar_propriedade.html', form=form)
        else:
            abort(403)
    else:
        abort(403)


@mod_component.route('/listar_modulos')
def listar_components():
    components = Component.query.filter((Component.tipo=='modulo') | (Component.tipo=='modulo_privado')).all()
    return render_template('component/listar_modulos.html', components=components)


@mod_component.route('/listar_modulos/<id_modulo>')
def listar_components_hierarquico(id_modulo):
    components = Component.query.filter((Component.tipo=='modulo') | (Component.tipo=='modulo_privado')).all()
    return render_template('component/listar_modulos.html', components=components)


@mod_component.route('/cadastrar/<id_component_pai>')
def cadastrar_component():
    pass


@mod_component.route('/listar_dispositivos/<id_leaf>')
def listar_dispositivos(id_leaf):
    dispositivos = Dispositivo.query.filter_by(id_leaf=id_leaf)
    return render_template('component/listar_modulos.html', dispositivos=dispositivos)


def alterar_interruptor():
    pass


def alterar_potenciometro():
    pass