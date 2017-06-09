from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import db
from app.models import *
from app.forms import ClientForm, DispositivoForm, ComponentForm

mod_dispositivo = Blueprint('dispositivo', __name__, url_prefix='/dispositivo', template_folder='templates')

@mod_dispositivo.route('/cadastrar/<id_leaf>', methods=['GET', 'POST'])
def cadastrar_dispositivo(id_leaf):
    form = DispositivoForm()
    if form.validate_on_submit():
        dispositivo = eval(form.tipo_dispositivo.data)(form.nome.data, form.porta.data)

        leaf_pai = Component.query.filter_by(id_component=id_leaf).first()
        if leaf_pai is None:
            flash('Erro no id do component escolhido')
            return redirect('/dashboard/')

        leaf_pai.add_dispositivo(dispositivo)

        db.session.add(dispositivo)
        db.session.commit()
        flash('Dispositivo criado com sucesso')

        return redirect('/dashboard/leaf/'+id_leaf)
    return render_template('dispositivo/cadastrar.html', form=form)


@mod_dispositivo.route('/atualizar/<id_dispositivo>')
def atualizar(id_dispositivo):
    return 'atualizar'


@mod_dispositivo.route('/alterar_interruptor/<id_dispositivo>')
def alterar_interruptor(id_dispositivo):
    return 'alterar interruptor'


@mod_dispositivo.route('alterar_potenciometro/<id_dispositivo>')
def alterar_potenciometro(id_dispositivo):
    return 'alterar potenciometro'