from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app.forms import LoginForm
from app.models import *

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard', template_folder='templates')


# @TODO fazer view index


@mod_dashboard.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
    return render_template('dashboard/index.html')


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
    return redirect(url_for('dashboard.index'))
