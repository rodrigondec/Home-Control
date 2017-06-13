from flask import render_template, Blueprint, session, abort, flash, redirect, url_for, request
from app.models import *
from app.forms import MonitorForm, RegraCondicaoAtuadorForm, RegraSensorInterruptorForm, RegraSensorPotenciometroForm, \
    RegraInterruptorInterruptorForm, RegraInterruptorPotenciometroForm, RegraPotenciometroInterruptorForm, \
    RegraPotenciometroPotenciometroForm

mod_monitor = Blueprint('monitor', __name__, url_prefix='/monitor', template_folder='templates')

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
def cadastrar_monitor(id_leaf):
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
        return render_template('monitor/cadastrar_monitor.html', form=form, leaf=leaf)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_monitor.route('/cadastrar_regra/<id_monitor>', methods=['GET', 'POST'])
def regra_condicao_atuador(id_monitor):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        monitor = Monitor.query.filter_by(id_monitor=id_monitor).first()
        if not monitor.leaf.alteravel_por(usuario):
            flash('Você não tem permissão para cadastrar uma regra para esse monitor')
            return redirect('/dashboard/')

        form = RegraCondicaoAtuadorForm(monitor.leaf_id)
        if form.validate_on_submit():
            return redirect('/monitor/cadastrar_regra/'+id_monitor+'/'+str(form.dispositivo_condicao.data)+'/'+str(form.dispositivo_atuador.data))
        return render_template('monitor/regra_condicao_atuador.html', form=form, monitor=monitor)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_monitor.route('/cadastrar_regra/<id_monitor>/<id_dispositivo_condicao>/<id_dispositivo_atuador>', methods=['GET', 'POST'])
def regra_dispositivo(id_monitor, id_dispositivo_condicao, id_dispositivo_atuador):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        monitor = Monitor.query.filter_by(id_monitor=id_monitor).first()
        dispositivo_condicao = Dispositivo.query.filter_by(id_dispositivo=id_dispositivo_condicao).first()
        dispositivo_atuador = Dispositivo.query.filter_by(id_dispositivo=id_dispositivo_atuador).first()

        if not monitor.leaf.alteravel_por(usuario):
            flash('Você não tem permissão para cadastrar uma regra para esse monitor')
            return redirect('/dashboard/')

        form = RegraInterruptorInterruptorForm(dispositivo_condicao, dispositivo_atuador)

        if dispositivo_condicao.tipo == 'sensor' and dispositivo_atuador.tipo == 'interruptor':
            form = RegraSensorInterruptorForm(dispositivo_condicao, dispositivo_atuador)
        elif dispositivo_condicao.tipo == 'sensor' and dispositivo_atuador.tipo == 'potenciometro':
            form = RegraSensorPotenciometroForm(dispositivo_condicao, dispositivo_atuador)
        elif dispositivo_condicao.tipo == 'interruptor' and dispositivo_atuador.tipo == 'interruptor':
            form = RegraInterruptorInterruptorForm(dispositivo_condicao, dispositivo_atuador)
        elif dispositivo_condicao.tipo == 'interruptor' and dispositivo_atuador.tipo == 'potenciometro':
            form = RegraInterruptorPotenciometroForm(dispositivo_condicao, dispositivo_atuador)
        elif dispositivo_condicao.tipo == 'potenciometro' and dispositivo_atuador.tipo == 'interruptor':
            form = RegraPotenciometroInterruptorForm(dispositivo_condicao, dispositivo_atuador)
        elif dispositivo_condicao.tipo == 'potenciometro' and dispositivo_atuador.tipo == 'potenciometro':
            form = RegraPotenciometroPotenciometroForm(dispositivo_condicao, dispositivo_atuador)

        if form.validate_on_submit():
            if form.cronometrado.data:
                if dispositivo_condicao.tipo == 'sensor':
                    condicao = CondicaoSensorCronometrada(dispositivo_condicao, form.valor_inicial_condicao.data,
                                                          form.valor_final_condicao.data, form.hora.data,
                                                          form.minuto.data)
                elif dispositivo_condicao.tipo == 'interruptor':
                    condicao = CondicaoInterriuptorCronometrada(dispositivo_condicao, form.valor_condicao.data,
                                                                form.hora.data, form.minuto.data)
                else:
                    condicao = CondicaoPotenciometroCronometrada(dispositivo_condicao, form.valor_inicial_condicao.data,
                                                                 form.valor_final_condicao.data, form.hora.data,
                                                                 form.minuto.data)
            else:
                if dispositivo_condicao.tipo == 'sensor':
                    condicao = CondicaoSensor(dispositivo_condicao, form.valor_inicial_condicao.data,
                                              form.valor_final_condicao.data)
                elif dispositivo_condicao.tipo == 'interruptor':
                    condicao = CondicaoInterruptor(dispositivo_condicao, form.valor_condicao.data)
                else:
                    condicao = CondicaoPotenciometro(dispositivo_condicao, form.valor_inicial_condicao.data,
                                                     form.valor_final_condicao.data)


            if dispositivo_atuador.tipo == 'interruptor':
                atuador = AtuadorInterruptor(dispositivo_atuador, form.valor_atuador.data)
            else:
                atuador = AtuadorPotenciometro(dispositivo_atuador, form.valor_atuador.data)

            regra = Regra(monitor, condicao, atuador)

            db.session.commit()
            return redirect('/monitor/' + str(monitor.leaf_id))
        return render_template('monitor/regra_valor.html', form=form, monitor=monitor, dispositivo_condicao=dispositivo_condicao, dispositivo_atuador=dispositivo_atuador)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')