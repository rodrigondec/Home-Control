from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app.models import *
from app.forms import MonitorForm

mod_monitor = Blueprint('monitor', __name__, url_prefix='/monitor', template_folder='templates')
# @TODO fazer metodos controlador monitor
# @TODO fazer views monitor

@mod_monitor.route('/<id_leaf>')
def monitor(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.acessivel_por(usuario):
            flash('Você não tem permissão para acessar o monitor desse leaf')
            return redirect('/dashboard/')
        if leaf.monitor is None:
            flash('Cadastre um monitor')
            return redirect('/monitor/cadastrar/'+id_leaf)
        return render_template('monitor/monitor.html/', leaf=leaf)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_monitor.route('/cadastrar/<id_leaf>', methods=['GET', 'POST'])
def cadastrar(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.alteravel_por(usuario):
            flash('Você não tem permissão para cadastrar um monitor para esse leaf')
            return redirect('/dashboard/')

        form = MonitorForm()
        if form.validate_on_submit():
            monitor = eval(form.tipo_monitor.data)(form.nome.data)

            leaf.monitor = monitor

            db.session.add(monitor)
            db.session.commit()
            flash('Monitor criado com sucesso')

            return redirect('/dashboard/leaf/'+id_leaf)
        return render_template('monitor/cadastrar_monitor.html', form=form)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')
