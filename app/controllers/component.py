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
        admin = Administrador.query.filter_by(id_administrador=session['id_usuario']).first()
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


def listar_modulos():
    pass


def listar_dispositivos():
    pass


def alterar_interruptor():
    pass


def alterar_potenciometro():
    pass
