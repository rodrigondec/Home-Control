from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import db
from app.models import *
from app.forms import ClientForm, DispositivoForm, ComponentForm

mod_component = Blueprint('component', __name__, url_prefix='/component', template_folder='templates')
# @TODO fazer metodos controlador component
# @TODO fazer views component


@mod_component.route('/')
def listar_components():
    components = Component.query.all()
    return render_template('component/listar_components.html', components=components)


@mod_component.route('/listar_components/<id_modulo>')
def listar_components_por_modulo(id_modulo):
    components = Component.query.filter((Component.tipo=='modulo') | (Component.tipo=='modulo_privado')).all()
    return render_template('component/listar_components.html', components=components)


@mod_component.route('/listar_dispositivos/<id_leaf>')
def listar_dispositivos_por_leaf(id_leaf):
    dispositivos = Dispositivo.query.filter_by(leaf_id=id_leaf)
    return render_template('component/listar_dispositivos.html', dispositivos=dispositivos)


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
                return redirect(url_for('component.listar_components'))
            return render_template('component/cadastrar_propriedade.html', form=form)
        else:
            abort(403)
    else:
        abort(403)


@mod_component.route('/cadastrar/<id_component_pai>', methods=['GET', 'POST'])
def cadastrar_component(id_component_pai):
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
            return redirect(url_for('component.listar_components'))

        component_pai.add_component(component)

        db.session.add(component)
        db.session.commit()
        flash('Cmponent criado com sucesso')

        return redirect(url_for('component.listar_components'))
    return render_template('component/cadastrar_component.html', form=form)

@mod_component.route('/<id_leaf>/dispositivo/cadastrar/', methods=['GET', 'POST'])
def cadastrar_dispositivo(id_leaf):
    form = DispositivoForm()
    if form.validate_on_submit():
        if form.tipo_dispositivo.data == 'Sensor':
            dispositivo = Sensor(form.porta.data)
        elif form.tipo_dispositivo.data == 'Interruptor':
            dispositivo = Interruptor(form.porta.data)
        else:
            dispositivo = Potenciometro(form.porta.data)

        leaf_pai = Leaf.query.filter_by(id_component=id_leaf).first()
        if leaf_pai is None:
            flash('Erro no id do component escolhido')
            return redirect(url_for('component.listar_components'))

        leaf_pai.add_dispositivo(dispositivo)

        db.session.add(dispositivo)
        db.session.commit()
        flash('Dispositivo criado com sucesso')

        return redirect('/component/listar_dispositivos/'+id_leaf)
    return render_template('component/cadastrar_dispositivo.html', form=form)


def atualizar_dispositivo(id_dispositivo):
    pass


@mod_component.route('/alterar_interruptor/<id_dispositivo>')
def alterar_interruptor(id_dispositivo):
    pass


@mod_component.route('alterar_potenciometro/<id_dispositivo>')
def alterar_potenciometro(id_dispositivo):
    pass
