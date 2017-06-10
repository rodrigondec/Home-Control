from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app.forms import MonitorForm

mod_monitor = Blueprint('monitor', __name__, url_prefix='/monitor', template_folder='templates')
# @TODO fazer metodos controlador monitor
# @TODO fazer views monitor

@mod_monitor.route('/<id_leaf>')
def monitor(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_monitor.route('/cadastrar/<id_leaf>')
def cadastrar(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.alteravel_por(usuario):
            flash('Você não tem permissão para cadastrar um monitor para esse leaf')
            return redirect('/dashboard/')

        form = MonitorForm()
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')
