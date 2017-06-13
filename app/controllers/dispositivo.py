from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import db
from app.models import *
from app.forms import ClientForm, DispositivoForm, ComponentForm, EmbarcadoForm, AlterarInterruptorForm, AlterarPotenciometroForm

mod_dispositivo = Blueprint('dispositivo', __name__, url_prefix='/dispositivo', template_folder='templates')

@mod_dispositivo.route('/cadastrar/<id_leaf>', methods=['GET', 'POST'])
def cadastrar_dispositivo(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.alteravel_por(usuario):
            flash('Você não pode adicionar dispositivos à esse leaf')
            return redirect('/dashboard/')

        form = DispositivoForm()
        if form.validate_on_submit():
            dispositivo = eval(form.tipo_dispositivo.data)(form.nome.data, form.porta.data)

            leaf.add_dispositivo(dispositivo)

            db.session.add(dispositivo)
            db.session.commit()
            flash('Dispositivo criado com sucesso')

            return redirect('/dashboard/leaf/'+id_leaf)
        return render_template('dispositivo/cadastrar_dispositivo.html', form=form, leaf=leaf)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dispositivo.route('/embarcado/<id_leaf>', methods=['GET', 'POST'])
def embarcado(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if leaf.embarcado is None:
            flash('Cadastre um embarcado')
            return redirect('/dispositivo/cadastrar_embarcado/'+id_leaf)
        return render_template('dispositivo/embarcado.html/', leaf=leaf)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dispositivo.route('/cadastrar_embarcado/<id_leaf>', methods=['GET', 'POST'])
def cadastrar_embarcado(id_leaf):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        leaf = Component.query.filter_by(id_component=id_leaf).first()
        if not leaf.alteravel_por(usuario):
            flash('Você não pode adicionar dispositivos à esse leaf')
            return redirect('/dashboard/')

        form = EmbarcadoForm()
        if form.validate_on_submit():
            embarcado = Embarcado(form.ip.data, form.mac.data)

            leaf.embarcado = embarcado

            db.session.add(embarcado)
            db.session.commit()
            flash('Embarcado criado com sucesso')

            return redirect('/dashboard/leaf/'+id_leaf)
        return render_template('dispositivo/cadastrar_embarcado.html', form=form, leaf=leaf)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')


@mod_dispositivo.route('/atualizar/<id_dispositivo>')
def atualizar(id_dispositivo):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        dispositivo = Dispositivo.query.filter_by(id_dispositivo=id_dispositivo).first()
        if not dispositivo.leaf.acessivel_por(usuario):
            flash('Você não tem autorização para alterar esse dispositivo')
            return redirect('/dashboard/')
        command = Command.query.filter_by(tipo='atualizar_dispositivo').first()
        command.before_execute(embarcado=dispositivo.leaf.embarcado, dispositivo=dispositivo)
        command.execute()
        return redirect('/dashboard/leaf/'+str(dispositivo.leaf_id))
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')

@mod_dispositivo.route('/alterar/<id_dispositivo>', methods=['GET', 'POST'])
def alterar(id_dispositivo):
    if 'logged_in' in session:
        usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
        dispositivo = Dispositivo.query.filter_by(id_dispositivo=id_dispositivo).first()
        if not dispositivo.leaf.alteravel_por(usuario):
            flash('Você não pode alterar essa leaf')
            return redirect('/dashboard/')

        if dispositivo.tipo == 'interruptor':
            form = AlterarInterruptorForm()
        else:
            form = AlterarPotenciometroForm()

        if form.validate_on_submit():
            command = Command.query.filter_by(tipo='alterar_dispositivo').first()
            command.before_execute(dispositivo.leaf.embarcado, dispositivo, form.valor.data, usuario.id_usuario)
            command.execute()
            return redirect('/dashboard/leaf/' + str(dispositivo.leaf_id))
        return render_template('dispositivo/alterar_dispositivo.html', form=form, dispositivo=dispositivo)
    else:
        flash('Entre no sistema primeiro!')
        return redirect('/')
